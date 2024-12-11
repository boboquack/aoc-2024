s=INPUT.split('\n')
l=[int(i.split()[0]) for i in s]
r=[int(i.split()[1]) for i in s]
l.sort()
r.sort()
print(sum(abs(i-j) for i,j in zip(l,r)))

d={}
for i in r:
    if i in d:d[i]+=1
    else:d[i]=1
x=0
for i in l:
    if i in d:x+=i*d[i]
print(x)
