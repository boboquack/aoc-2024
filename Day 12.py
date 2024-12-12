s=INPUT.split()
ss=SAMPLE.split()
from collections import defaultdict as dd
h=len(s)
w=len(s[0])
d=dd(lambda:'.')
for r in range(h):
    for c in range(w):
        d[(r,c)]=s[r][c]

l=dd(lambda:False)
ddd=[(0,1),(1,0),(0,-1),(-1,0)]
f=lambda x:((x[0]+dx,x[1]+dy) for dx,dy in ddd)
price=0
for r in range(h):
    for c in range(w):
        if l[(r,c)]:continue
        x=d[(r,c)]
        todo=[(r,c)]
        found={(r,c)}
        perim=0
        while todo:
            y=todo.pop()
            for y2 in f(y):
                if y2 not in found and d[y2]==x:
                    found.add(y2)
                    todo.append(y2)
                    l[y2]=True
                elif d[y2]!=x:
                    perim+=1
        price+=len(found)*perim
print(price)
l=dd(lambda:False)
price=0
for r in range(h):
    for c in range(w):
        if l[(r,c)]:continue
        x=d[(r,c)]
        todo=[(r,c)]
        found={(r,c)}
        perim=[]
        while todo:
            y=todo.pop()
            for y2,k in zip(f(y),range(4)):
                if y2 not in found and d[y2]==x:
                    found.add(y2)
                    todo.append(y2)
                    l[y2]=True
                elif d[y2]!=x:
                    if k%2==0:perim.append((k,*y2[::-1]))
                    else:perim.append((k,*y2))
        perim.sort()
        pp=1
        for i in range(1,len(perim)):
            if perim[i][0]!=perim[i-1][0] or abs(perim[i][1]-perim[i-1][1])+abs(perim[i][2]-perim[i-1][2])!=1:
                pp+=1
        price+=len(found)*pp
print(price)
