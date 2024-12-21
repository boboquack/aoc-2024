s=INPUT.split()
ss=SAMPLE.split()
locs={'0':(-1,0),'1':(-2,1),'2':(-1,1),'3':(0,1),'4':(-2,2),'5':(-1,2),
      '6':(0,2),'7':(-2,3),'8':(-1,3),'9':(0,3),'A':(0,0),'^':(-1,0),
      '<':(-2,-1),'v':(-1,-1),'>':(0,-1)}
def comp(s,n):
    for _ in range(n):
        l=[]
        cx,cy=0,0
        for c in s:
            gx,gy=locs[c]
            x,y=gx-cx,gy-cy
            if x==y==0:l.append('A')
            elif x==0 and y>0:
                l.append('^'*y+'A')
            elif x==0 and y<0:
                l.append('v'*-y+'A')
            elif y==0 and x<0:
                l.append('<'*-x+'A')
            elif y==0 and x>0:
                l.append('>'*x+'A')
            elif y>0 and x>0:
                l.append('>'*x+'^'*y+'A')
            elif y>0 and x<0 and (cy!=0 or gx!=-2):
                l.append('<'*-x+'^'*y+'A')
            elif y>0 and x<0:
                l.append('^'*y+'<'*-x+'A')
            elif y<0 and x>0 and (cx!=-2 or gy!=0):
                l.append('v'*-y+'>'*x+'A')
            elif y<0 and x>0:
                l.append('>'*x+'v'*-y+'A')
            elif (cy!=0 or gx!=-2):
                l.append('<'*-x+'v'*-y+'A')
            else:
                l.append('v'*-y+'<'*-x+'A')
            cx,cy=gx,gy
        s=''.join(l)
        #print(len(s),s)
    return len(s)
print(sum(comp(i,3)*int(i[:-1]) for i in s))
from collections import defaultdict as dd
def do(t):
    global K,npairs
    npairs[('A',t[0])]+=K
    for i,j in zip(t,t[1:]):
        npairs[(i,j)]+=K
def comp(s,n):
    global K,npairs
    pairs=dd(int)
    pairs[('A',s[0])]+=1
    for pair in zip(s,s[1:]):
        pairs[pair]+=1
    for _ in range(n):
        l=[]
        cx,cy=0,0
        npairs=dd(int)
        for pair in pairs:
            K=pairs[pair]
            cx,cy=locs[pair[0]]
            gx,gy=locs[pair[1]]
            x,y=gx-cx,gy-cy
            if x==y==0:do('A')
            elif x==0 and y>0:
                do('^'*y+'A')
            elif x==0 and y<0:
                do('v'*-y+'A')
            elif y==0 and x<0:
                do('<'*-x+'A')
            elif y==0 and x>0:
                do('>'*x+'A')
            elif y>0 and x>0 and (cx!=-2 or gy!=0):
                do('^'*y+'>'*x+'A')
            elif y>0 and x>0:
                do('>'*x+'^'*y+'A')
            elif y>0 and x<0 and (cy!=0 or gx!=-2):
                do('<'*-x+'^'*y+'A')
            elif y>0 and x<0:
                do('^'*y+'<'*-x+'A')
            elif y<0 and x>0 and (cx!=-2 or gy!=0):
                do('v'*-y+'>'*x+'A')
            elif y<0 and x>0:
                do('>'*x+'v'*-y+'A')
            elif (cy!=0 or gx!=-2):
                do('<'*-x+'v'*-y+'A')
            else:
                do('v'*-y+'<'*-x+'A')
        pairs=npairs
    return sum(pairs[i] for i in pairs)
print(sum(comp(i,3)*int(i[:-1]) for i in s))
print(sum(comp(i,26)*int(i[:-1]) for i in s))
