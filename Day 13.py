s=INPUT.split('\n\n')
ss=SAMPLE.split('\n\n')
t=0
for i in s:
    x,y,z=i.split('\n')
    w1,w2=x.split()[-2:]
    w1=int(w1[2:-1])
    w2=int(w2[2:])
    v1,v2=y.split()[-2:]
    v1=int(v1[2:-1])
    v2=int(v2[2:])
    u1,u2=z.split()[-2:]
    u1=int(u1[2:-1])
    u2=int(u2[2:])
    m=10000
    for k in range(100):
        for l in range(100):
            if k*w1+l*v1==u1 and k*w2+l*v2==u2:
                m=min(m,3*k+l)
    if m<10000:
        t+=m
print(t)
from sympy import solve
from sympy.abc import k,l
from math import gcd
t=0
for i in s:
    x,y,z=i.split('\n')
    w1,w2=x.split()[-2:]
    w1=int(w1[2:-1])
    w2=int(w2[2:])
    v1,v2=y.split()[-2:]
    v1=int(v1[2:-1])
    v2=int(v2[2:])
    u1,u2=z.split()[-2:]
    u1=int(u1[2:-1])+10000000000000
    u2=int(u2[2:])+10000000000000
    x=solve([k*w1+l*v1-u1,k*w2+l*v2-u2],k,l)
    a=int(x[k])
    b=int(x[l])
    if a*w1+b*v1==u1 and a*w2+b*v2==u2:
        if w2*v1==v2*w1:
            g=math.gcd(w1,v1)
            r=v1//g
            s=w1//g
            if 3*r>s:
                u=a//r
                a-=u*r
                b+=u*s
            elif 3*r<s:
                u=a//s
                a+=u*r
                b-=u*s
        t+=3*a+b
print(t)
