tows=INPUT1.replace(' ','').split(',')
pats=INPUT2.split()

def f(pat):
    l=[1]+[0]*len(pat)
    for i in range(1,len(pat)+1):
        for tow in tows:
            if len(tow)>i:continue
            if pat[i-len(tow):i]==tow:
                l[i]+=l[i-len(tow)]
    return l[-1]

print(sum(f(pat)>0 for pat in pats))
print(sum(f(pat) for pat in pats))
