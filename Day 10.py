s=INPUT.split()
sss=SAMPLE2.split()
ss=SAMPLE1.split()
import collections
d=collections.defaultdict(lambda:-1)
h=len(s)
w=len(s[0])
e=[[] for i in range(10)]
for r in range(h):
    for c in range(w):
        d[(r,c)]=int(s[r][c])
        e[int(s[r][c])].append((r,c))
l=collections.defaultdict(set)
for j in e[0]:
    l[j]={j}
t=0
ds=[(0,1),(1,0),(0,-1),(-1,0)]
for i in range(1,10):
    for j in e[i]:
        x,y=j
        for dx,dy in ds:
            if d[(x+dx,y+dy)]==i-1:
                l[j]|=l[(x+dx,y+dy)]
        if i==9:
            t+=len(l[j])
print(t)
l=collections.defaultdict(lambda:0)
for j in e[0]:
    l[j]=1
t=0
ds=[(0,1),(1,0),(0,-1),(-1,0)]
for i in range(1,10):
    for j in e[i]:
        x,y=j
        for dx,dy in ds:
            if d[(x+dx,y+dy)]==i-1:
                l[j]+=l[(x+dx,y+dy)]
        if i==9:
            t+=l[j]
print(t)
