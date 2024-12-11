s=INPUT
l=[]
k=0
b=0
x=0
for i in s:
    if b:
        for j in range(int(i)):l.append(None)
        x+=int(i)
    else:
        for j in range(int(i)):l.append(k)
        k+=1
    b=1-b

i=0
while x:
    c=l.pop()
    if c is not None:
        while l[i] is not None:
            i+=1
        l[i]=c
    x-=1
v=0
for i in range(len(l)):
    v+=i*l[i]
print(v)

b=0
x=0
j=0
gaps=[]
files=[]
for i in s:
    if b:
        gaps.append((x,int(i)))
        x+=int(i)
    else:
        files.append((x,int(i),j))
        j+=1
        x+=int(i)
    b=1-b
v=0
for x,l,j in files[::-1]:
    for i in range(len(gaps)):
        y,ll=gaps[i]
        if y>x:break
        if ll>=l:
            gaps[i]=((y+l,ll-l))
            x=y
            break
    v+=sum(x+i for i in range(l))*j
print(v)
    
            
