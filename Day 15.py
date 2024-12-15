s=INPUT1.split('\n')
t=INPUT2.replace('\n','')
ss=SAMPLE1.split('\n')
tt=SAMPLE2
s=[list(i) for i in s]
h=len(s)
w=len(s[0])
for r in range(h):
    for c in range(w):
        if s[r][c]=='@':
            break
    else:continue
    break

dd={'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
for d in t:
    dr,dc=dd[d]
    r2,c2=r+dr,c+dc
    while s[r2][c2] not in '.#':
        r2,c2=r2+dr,c2+dc
    if s[r2][c2]=='.':
        s[r][c]='.'
        s[r2][c2]='O'
        r,c=r+dr,c+dc
        s[r][c]='@'
a=0
for r in range(h):
    for c in range(w):
        if s[r][c]=='O':a+=100*r+c
print(a)
s=INPUT1.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.').split('\n')
ss=SAMPLE3.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.').split('\n')
tt=SAMPLE4.replace('\n','')
s=[list(i) for i in s]
h=len(s)
w=len(s[0])
for r in range(h):
    for c in range(w):
        if s[r][c]=='@':
            break
    else:continue
    break
for d in t:
    dr,dc=dd[d]
    rc=[(r+dr,c+dc)]
    upl=[]
    upr=[]
    while any(s[r2][c2]!='.' for r2,c2 in rc):
        if any(s[r2][c2]=='#' for r2,c2 in rc):break
        nrc=[]
        for r2,c2 in rc:
            if s[r2][c2]=='[':
                if dr!=0:
                    nrc.append((r2+dr,c2+dc))
                    nrc.append((r2+dr,c2+dc+1))
                else:nrc.append((r2,c2+2*dc))
                upl.append((r2,c2))
                upr.append((r2,c2+1))
            if s[r2][c2]==']':
                if dr!=0:
                    nrc.append((r2+dr,c2+dc))
                    nrc.append((r2+dr,c2+dc-1))
                else:nrc.append((r2,c2+2*dc))
                upl.append((r2,c2-1))
                upr.append((r2,c2))
        rc=nrc
    else:
        s[r][c]='.'
        for r2,c2 in upl+upr:s[r2][c2]='.'
        for r2,c2 in upl:s[r2+dr][c2+dc]='['
        for r2,c2 in upr:s[r2+dr][c2+dc]=']'
        r,c=r+dr,c+dc
        s[r][c]='@'
a=0
for r in range(h):
    for c in range(w):
        if s[r][c]=='[':a+=100*r+c  
print(a)
