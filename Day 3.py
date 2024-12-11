s=INPUT

import re
x=re.findall(r'mul\((\d+),(\d+)\)',s)
t=0
for m in x:
    a=m[0]
    b=m[1]
    t+=int(a)*int(b)
print(t)

x=re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))",s)
t=0
ok=True
for m in x:
    if m[0]=="don't()":
        ok=False
    elif m[0]=="do()":
        ok=True
    elif ok:
        t+=int(m[1])*int(m[2])
print(t)
