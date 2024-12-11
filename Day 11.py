s=INPUT.split()
s=[int(i) for i in s]
for i in range(25):
    t=[]
    for i in s:
        if i==0:t.append(1)
        elif len(str(i))%2==0:
            t.append(int(str(i)[:len(str(i))//2]))
            t.append(int(str(i)[len(str(i))//2:]))
        else:
            t.append(i*2024)
    s=t
print(len(t))

s=INPUT.split()
s={int(i):1 for i in s}
from collections import defaultdict as dd
for i in range(75):
    t=dd(int)
    for i in s:
        if i==0:t[1]+=s[i]
        elif len(str(i))%2==0:
            t[int(str(i)[:len(str(i))//2])]+=s[i]
            t[int(str(i)[len(str(i))//2:])]+=s[i]
        else:
            t[i*2024]+=s[i]
    s=t
print(sum(t[i] for i in t))
