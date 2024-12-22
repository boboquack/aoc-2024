s=INPUT.split()
ss=SAMPLE2.split()
s=[int(i) for i in s]

def mix(a,b):return a^b
def prune(a):return a%16777216
def new(a):
    a=prune(mix(a,a*64))
    a=prune(mix(a,a//32))
    a=prune(mix(a,a*2048))
    return a
t=0
for i in s:
    for _ in range(2000):i=new(i)
    t+=i
print(t)
from collections import defaultdict as dd
d=dd(int)
for i in s:
    l=[i]
    for _ in range(2000):l.append(new(l[-1]))
    p=[i%10 for i in l]
    c=[j-i for i,j in zip(p,p[1:])]
    f=set()
    for d1,d2,d3,d4,x in zip(c,c[1:],c[2:],c[3:],p[4:]):
        if (d1,d2,d3,d4) not in f:
            f.add((d1,d2,d3,d4))
            d[(d1,d2,d3,d4)]+=x
print(max(d[i] for i in d))
    
