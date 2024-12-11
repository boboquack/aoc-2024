s=INPUT.split('\n\n')
s,t=s
s=s.split()
t=t.split()
s=[tuple(map(int,i.split('|'))) for i in s]
t=[tuple(map(int,i.split(','))) for i in t]
u=0
for i in t:
    for a,b in s:
        if a not in i or b not in i or i.index(a)<i.index(b):pass
        else:break
    else:
        u+=i[len(i)//2]
print(u)
u=0
p=list({a[0] for a in s}|{a[1] for a in s})
def sort(p):
    if len(p)<=1:return p
    x=p[0]
    y=[]
    z=[]
    for a,b in s:
        if b==x and a in p:y.append(a)
        elif a==x and b in p:z.append(b)
    v=[]
    for w in p[1:]:
        if w not in y and w not in z:
            v.append(w)
    assert not v
    return sort(y)+[x]+sort(z)
o=sort(p)
for i in t:
    for a,b in s:
        if a not in i or b not in i or i.index(a)<i.index(b):pass
        else:break
    else:
        continue
    #i=list(i)
    #for j in range(len(i)):
    #    for k in range(len(i)-1):
    #        if o.index(i[k])>o.index(i[k+1]):
    #            i[k],i[k+1]=i[k+1],i[k]
    i=sort(i)
    u+=i[len(i)//2]
print(u)
    

