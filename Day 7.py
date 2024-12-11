s=INPUT.split('\n')

x=0
for i in s:
    t=i.split(':')
    n=int(t[0])
    y=t[1].strip()
    if not all(i in '0123456789 ' for i in y):raise ValueError
    for j in range(2**(y.count(' '))):
        z='('*y.count(' ')
        k=0
        for i in y:
            if i==' ':
                if j&(2**k):z+=')*'
                else:z+=')+'
                k+=1
            else:z+=i
        if eval(z)==n:
            x+=n
            break
print(x)

def check(x,s=None):
    if len(x)==0:return s
    
    v=int(x[0])
    if s==None:
        return check(x[1:],{v})
    p=10**len(x[0])
    return check(x[1:],{a+v for a in s}|{a*v for a in s}|{a*p+v for a in s})

x=0
for i in s:
    t=i.split(':')
    n=int(t[0])
    y=t[1].strip()
    if not all(i in '0123456789 ' for i in y):raise ValueError
    if any(i==n for i in check(y.split())):
        x+=n
print(x)
