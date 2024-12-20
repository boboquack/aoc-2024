s=INPUT.split()
ss=SAMPLE.split()
from collections import defaultdict as dd
g=dd(int)
h=len(s)
w=len(s[0])
for r in range(h):
    for c in range(w):
        g[(r,c)]=0 if s[r][c]=='#' else 1
        if s[r][c]=='S':
            sr,sc=r,c
        if s[r][c]=='E':
            er,ec=r,c
from math import inf
dists=dd(lambda:inf)
new=[(sr,sc,0)]
ds=[(1,0),(-1,0),(0,1),(0,-1)]
i=0
while i<len(new):
    r,c,dt=new[i]
    i+=1
    if g[(r,c)]==0:continue
    dists[(r,c)]=dt
    for dr,dc in ds:
        if (r+dr,c+dc) not in dists:
            new.append((r+dr,c+dc,dt+1))
best=dists[(er,ec)]
ans=0
ds2=[(*i,1) for i in ds]+[(0,0,0)]
for r1 in range(h):
    for c1 in range(w):
        for dr,dc in ds:
            r2,c2=r1+dr,c1+dc
            a=min(dists[(r1+dr,c1+dc)]+di for dr,dc,di in ds2)
            #b=min(dists[(r2+dr,c2+dc)] for dr,dc,di in ds2)
            b=dists[(r2,c2)]
            if 0<=a<b<=best and a+(best-b)+1<=best-100:
                ans+=1
print(ans)
ans=0
def bad(r1,c1,r2,c2,e1,e2):
    return False
ds3=[(x,y,abs(x)+abs(y)) for x in range(-20,21) for y in range(-20,21) if abs(x)+abs(y)<=20]
for r1 in range(h):
    for c1 in range(w):
        for dr,dc,i2 in ds3:
            r2,c2=r1+dr,c1+dc
            a=dists[(r1,c1)]
            b=dists[(r2,c2)]
            if 0<=a<b<=best and a+(best-b)+i2<=best-100:
                ans+=1
print(ans)
