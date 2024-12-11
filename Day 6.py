s=INPUT.split()
import collections
d=collections.defaultdict(int)
h=len(s)
w=len(s[0])
for i in range(h):
    for j in range(w):
        d[(i,j)]=2 if s[i][j]=='#' else 1
        if s[i][j]=='^':
            x=i
            y=j
r=(-1,0)          
t={(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
found=set()
state=set()
while (r,x,y) not in state:
    state.add((r,x,y))
    found.add((x,y))
    dx,dy=r
    while d[(x+dx,y+dy)]==2:
        r=t[r]
        dx,dy=r
    x+=dx
    y+=dy
    if d[(x,y)]==0:break
print(len(found))
v=0
for a in range(h):
    for b in range(w):
        if s[a][b]!='.':continue
        d=collections.defaultdict(int)
        for i in range(h):
            for j in range(w):
                d[(i,j)]=2 if s[i][j]=='#' else 1
                if s[i][j]=='^':
                    x=i
                    y=j
        d[(a,b)]=2
        r=(-1,0)          
        t={(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
        found=set()
        state=set()
        while (r,x,y) not in state:
            state.add((r,x,y))
            found.add((x,y))
            dx,dy=r
            while d[(x+dx,y+dy)]==2:
                r=t[r]
                dx,dy=r
            x+=dx
            y+=dy
            if d[(x,y)]==0:break
        else:
            v+=1
    print('... up to',a,'out of',h)
print(v)
