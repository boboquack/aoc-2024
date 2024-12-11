s=INPUT.split('\n')

t=0
for i in s:
    l=map(int,i.split())
    l=list(l)
    if (all(i<j for i,j in zip(l,l[1:])) or all(i>j for i,j in zip(l,l[1:])) ) and all(1<=abs(i-j)<=3 for i,j in zip(l,l[1:])):
        t+=1
print(t)

t=0
for i in s:
    l=map(int,i.split())
    l=list(l)
    
    if (all(i<j for i,j in zip(l,l[1:])) or all(i>j for i,j in zip(l,l[1:])) ) and all(1<=abs(i-j)<=3 for i,j in zip(l,l[1:])):
        t+=1
    else:
        u=l
        for j in range(len(u)):
            l=u[:j]+u[j+1:]
            if (all(i<j for i,j in zip(l,l[1:])) or all(i>j for i,j in zip(l,l[1:])) ) and all(1<=abs(i-j)<=3 for i,j in zip(l,l[1:])):
                t+=1
                break
print(t)
