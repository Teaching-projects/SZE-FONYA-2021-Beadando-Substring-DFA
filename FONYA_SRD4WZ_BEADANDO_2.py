pip install pythomata
pip install pysimpleautomata
pip install graphviz
def pi_prefix_fuggveny(p):
    P = list(p)
    m = len(p)
    a = [0] * m
    k = 0

    for q in range(2, m + 1):
        while k > 0 and P[k] != P[q - 1]:
            k = a[k - 1]
        if P[k] == P[q - 1]:
            k += 1
        a[q - 1] = k

    return a

def TransitionFunction(a,s):
    transition_function={}
    PI=[]
    seged='s0'
    sv=True
    PI=pi_prefix_fuggveny(a)
    for i in range(s):
        transition_function["s"+str(i)] = {}
    transition_function["s0"]= {a[0]:"s1", Ellentett(a[0]):"s0"}
    for i in range(1,len(a)):
        seged=transition_function['s0'][Ellentett(a[i])]
        if((PI[i-1]>=PI[i])&sv is True): 
            seged='s'+str(i)
            sv=False
        
        transition_function["s"+str(i)]= {a[i]:"s"+str(i+1), Ellentett(a[i]):str(seged)}
    transition_function['s'+str(len(a))]={'a':'s'+str(len(a)),'b':'s'+str(len(a))}
    print (PI)
    print(transition_function)
    return transition_function

def Ellentett(a):
    if a == "a": return "b"
    else: return "a"

from graphviz import Digraph
from graphviz import Graph
G=False
while G is False:
    a=input('Milyen (a,b) abc fölötti szót tartalmazó szavakat fogadjon el?\n')
    b= set(a)
    print (b)
    if b!={'b','a'}: 
        print('Nem megfelelő a kritérium! Adj meg másikat!')
    else: G=True
c=set()
PI=[]
for i in range(len(a)+1): c.add('s'+str(i))
b= set(a)
accepting_state= 's'+str(len(a))
from pythomata import SimpleDFA
alphabet = ('a','b')
states = c
initial_state = "s0"
accepting_states = {accepting_state}
if a[0]=='b': seged=a[0]
else: seged = 'b'
transition_function = TransitionFunction(a,len(c))

    

dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)
graph = dfa.minimize().trim().to_graphviz()
graph.render("DFA")
szo=input('Az előző feltételek alapján a vizsgálandó szó:\n')
print(dfa.accepts(szo))
while szo!='':
    szo=input('Az előző feltételek alapján a vizsgálandó szó:\n')
    print(dfa.accepts(szo))

