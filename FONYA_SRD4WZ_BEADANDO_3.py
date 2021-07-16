#!/usr/bin/env python
# coding: utf-8

pip install imageio

from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
import imageio

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

def PIellentett(a,b):
    a+=Ellentett(b)
    PI=pi_prefix_fuggveny(a)
    return PI[-1]

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
        seged='s'+str(PIellentett(a[:i],a[i]))
        transition_function["s"+str(i)]= {a[i]:"s"+str(i+1), Ellentett(a[i]):str(seged)}
    transition_function['s'+str(len(a))]={'a':'s'+str(len(a)),'b':'s'+str(len(a))}
    return transition_function

def Ellentett(a):
    if a == "a": return "b"
    else: return "a"

def gif(szo, dfa):
    images=[]
    filenames=[]
    for i in range(len(szo)+1):
        fname = "DFA_state_" + str(i)
        dfa.show_diagram(szo[0:i],fname)
        filenames.append(fname+".png")
    filenames[0]=filenames[-1]
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(szo+'.gif', images, fps=1)
    return ("A gif elkészült "+szo+" inputról")
    
states=set()
PI=[]
G=False
filenames=[]
images=[]
alphabet = ('a','b')

while G is False:
    a=input('Milyen (a,b) abc fölötti szót tartalmazó szavakat fogadjon el?\n')
    b= set(a)
    if b!={'b','a'}: 
        print('Nem megfelelő a kritérium! Adj meg másikat!')
    else: G=True

for i in range(len(a)+1): states.add('s'+str(i))
    
accepting_state= 's'+str(len(a))

transition_function = TransitionFunction(a,len(states))

dfa=VisualDFA(
    states=states,
    input_symbols={'a','b'},
    transitions=transition_function,
    initial_state="s0",
    final_states={accepting_state})

szo=input('Az előző feltételek alapján a vizsgálandó szó:\n')
print(gif(szo,dfa))

while szo!='':
    szo=input('Az előző feltételek alapján a vizsgálandó szó:\n')
    print(gif(szo,dfa))