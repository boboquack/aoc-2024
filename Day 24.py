s=INPUT1.split('\n')
t=INPUT2.split('\n')
ss=SAMPLE1.split('\n')
tt=SAMPLE2.split('\n')
d={}
for i in s:
    a,b=i.split(':')
    b=b.strip()
    d[a]=int(b)
from collections import defaultdict as dd
ref=dd(list)
for i in t:
    x,op,y,_,z=i.split()
    ref[(x,y)].append((op,z))
todo=[]
found=set()
for j,k in ref:
    if j in d and k in d:
        if (j,k) not in found:todo.append((j,k))
        found.add((j,k))
while todo:
    a,b=todo.pop()
    for o,c in ref[(a,b)]:
        if o=='AND':
            d[c]=d[a]&d[b]
        elif o=='OR':
            d[c]=d[a]|d[b]
        else:
            d[c]=d[a]^d[b]
        for i,j in ref:
            if i==c and j in d or j==c and i in d:
                if (i,j) not in found:
                    todo.append((i,j))
                    found.add((i,j))
u=0
for i in d:
    if i[0]=='z':
        x=int(i[1:])
        u+=d[i]*2**x
print(u)

d={}
todo=[]
found=set()
with open('ops.txt','w') as fout:
    for z in range(len(s)//2):
        a=str(z)
        if len(a)==1:a='0'+a
        d['x'+a]=0
        d['y'+a]=0
        for j,k in ref:
            if j in d and k in d:
                if (j,k) not in found:todo.append((j,k))
                found.add((j,k))
        while todo:
            a,b=todo.pop()
            for o,c in ref[(a,b)]:
                if o=='AND':
                    d[c]=d[a]&d[b]
                elif o=='OR':
                    d[c]=d[a]|d[b]
                else:
                    d[c]=d[a]^d[b]
                for i,j in ref:
                    if i==c and j in d or j==c and i in d:
                        if (i,j) not in found:
                            todo.append((i,j))
                            found.add((i,j))

def check(a1,a2,debug=False):
    if debug:fout=open('ops.txt','w')
    d={}
    todo=[]
    found=set()
    for z in range(len(s)//2):
        a=str(z)
        if len(a)==1:a='0'+a
        d['x'+a]=1 if a1&(2**z) else 0
        d['y'+a]=1 if a2&(2**z) else 0
        for j,k in ref:
            if j in d and k in d:
                if (j,k) not in found:todo.append((j,k))
                found.add((j,k))
        while todo:
            a,b=todo.pop()
            for o,c in ref[(a,b)]:
                if o=='AND':
                    d[c]=d[a]&d[b]
                elif o=='OR':
                    d[c]=d[a]|d[b]
                else:
                    d[c]=d[a]^d[b]
                if debug:fout.write(' '.join(str(i) for i in [c,'=',a,o,b,'|',d[a],o,d[b],'->',d[c],'\n']))
                for i,j in ref:
                    if i==c and j in d or j==c and i in d:
                        if (i,j) not in found:
                            todo.append((i,j))
                            found.add((i,j))
    if debug:fout.close()
    u=0
    for i in d:
        if i[0]=='z':
            x=int(i[1:])
            u+=d[i]*2**x
    return u

'''K=L=list(range(120,127))
for i in K:
    for j in L:
        if check(i,j)!=i+j:
            check(i,j,debug=True)
            raise ValueError'''
check(0,0,debug=True)
import networkx as nx
G=nx.DiGraph()
colours={}
for i in t:
    x,op,y,_,z = i.split()
    G.add_edges_from(((x,i),(y,i),(i,z)))
    if x[0]=='x':colours[x]='red'
    if y[0]=='y':colours[y]='green'
    if y[0]=='x':colours[y]='red'
    if x[0]=='y':colours[x]='green'
    colours[i]='blue' if op=='AND' else 'yellow' if op=='OR' else 'purple'
    colours[z]='brown' if z[0]=='z' else 'orange'
nx.draw_kamada_kawai(G,node_color=[colours[i] for i in G.nodes],with_labels=True)
from matplotlib import pyplot as plt
plt.show()

# strategy:
# - use matplotlib to find the two swaps that 
#    are obvious in the graph
# - use ops.txt to find the two places where gates 
#    are swapped around and check those positions 
#    in the graph (because I'm not observant enough 
#    to catch those swaps apparently: there is a 
#    colouring difference but I missed it)
#   - regex 1: z.*( AND| OR)   // catches the visual bugs 
#                              // + a transposal bug
#   - regex 2: (...) = x(..) XOR y\2(.|\n)*\1 OR 
#                   // catches a different transposal bug
