s=INPUT.split()
ss=SAMPLE.split()
h=len(s)
w=len(s[0])
for i in range(h):
    for j in range(w):
        if s[i][j]=='S':
            start=(i,j)
            todo=[(0,i,j,(0,1))]
            found=set()
        if s[i][j]=='E':
            goal=(i,j)
import heapq
lt={(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}
rt={(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}
while todo:
    x,r,c,d=heapq.heappop(todo)
    if (r,c)==goal:break
    if (r,c,d) in found:continue
    found.add((r,c,d))
    dr,dc=d
    dl=lt[d]
    dar=rt[d]
    if s[r+dr][c+dc]!='#':heapq.heappush(todo,(x+1,r+dr,c+dc,d))
    heapq.heappush(todo,(x+1000,r,c,dl))
    heapq.heappush(todo,(x+1000,r,c,dar))
print(x)
a=x

i,j=start
todo=[(0,i,j,(0,1),None)]
backs={}
dists={}
goals=set()
while todo:
    x,r,c,d,b=heapq.heappop(todo)
    if x>a:break
    if (r,c)==goal:goals.add((r,c,d))
    if (r,c,d) in backs:
        if dists[(r,c,d)]==x:
            backs[(r,c,d)].append(b)
        continue
    dists[(r,c,d)]=x
    backs[(r,c,d)]=[b]
    dr,dc=d
    dl=lt[d]
    dar=rt[d]
    if s[r+dr][c+dc]!='#':heapq.heappush(todo,(x+1,r+dr,c+dc,d,(r,c,d)))
    heapq.heappush(todo,(x+1000,r,c,dl,(r,c,d)))
    heapq.heappush(todo,(x+1000,r,c,dar,(r,c,d)))

do=set()
while goals:
    v=goals.pop()
    if v is None:continue
    do.add(v[:2])
    for i in backs[v]:
        goals.add(i)
print(len(do))
