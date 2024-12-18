s=INPUT.split()
B=70
ss=SAMPLE.split()
BB=6
ll=[tuple(map(int,i.split(','))) for i in s]
import heapq
dd=[(0,1),(0,-1),(-1,0),(1,0)]
def f(n):
    l=set(ll[:n])
    todo=[(0,0,0)]
    found={}
    while todo:
        d,x,y=heapq.heappop(todo)
        if (x,y) in found:continue
        if (x,y) in l:continue
        found[(x,y)]=d
        if (x,y)==(B,B):break
        for dx,dy in dd:
            if 0<=x+dx<=B and 0<=y+dy<=B:
                heapq.heappush(todo,(d+1,x+dx,y+dy))
    else:return -1
    return found[(B,B)]
print(f(1024))
lo=1
hi=len(ll)
while lo<hi:
    mid=(lo+hi)//2
    if f(mid)==-1:
        hi=mid
    else:
        lo=mid+1
print(ll[lo-1])
def v(n):
    l=set(ll[:n])
    todo=[(0,0,0)]
    found={}
    while todo:
        d,x,y=heapq.heappop(todo)
        if (x,y) in found:continue
        if (x,y) in l:continue
        found[(x,y)]=d
        for dx,dy in dd:
            if 0<=x+dx<=B and 0<=y+dy<=B:
                heapq.heappush(todo,(d+1,x+dx,y+dy))
    for i in range(B+1):
        print(''.join('#' if (i,j) in l else ('O' if (i,j) in found else '.') for j in range(B+1)))
    print()
