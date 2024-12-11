s=INPUT.split()
ss=SAMPLE.split()
#s=ss

h=len(s)
w=len(s[0])
d={}
for r in range(h):
    for c in range(w):
        if s[r][c]!='.':
            if s[r][c] in d:d[s[r][c]].append((r,c))
            else:d[s[r][c]]=[(r,c)]
a=set()
for i in d:
    for j in range(len(d[i])):
        for k in range(j+1,len(d[i])):
            x1,y1=d[i][j]
            x2,y2=d[i][k]
            a.add((2*x1-x2,2*y1-y2))
            a.add((2*x2-x1,2*y2-y1))

print(len([(x,y) for x,y in a if 0<=x<h and 0<=y<w]))

a=set()
for i in d:
    for j in range(len(d[i])):
        for k in range(j+1,len(d[i])):
            x1,y1=d[i][j]
            x2,y2=d[i][k]
            x,y=x1,y1
            while 0<=x+(x2-x1)<h and 0<=y+(y2-y1)<w:
                x+=x2-x1
                y+=y2-y1
                a.add((x,y))
            x,y=x2,y2
            while 0<=x+(x1-x2)<h and 0<=y+(y1-y2)<w:
                x+=x1-x2
                y+=y1-y2
                a.add((x,y))

print(len(a))
