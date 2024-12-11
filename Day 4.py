s=INPUT.split()
h=len(s)
w=len(s[0])
t=0
for i in range(h):
    for j in range(w-3):
        if s[i][j:j+4]=='XMAS':t+=1
        if s[i][j:j+4]=='SAMX':t+=1
for i in range(h-3):
    for j in range(w):
        if s[i][j]+s[i+1][j]+s[i+2][j]+s[i+3][j]=='XMAS':t+=1
        if s[i][j]+s[i+1][j]+s[i+2][j]+s[i+3][j]=='SAMX':t+=1
for i in range(h-3):
    for j in range(w-3):
        if s[i][j]+s[i+1][j+1]+s[i+2][j+2]+s[i+3][j+3]=='XMAS':t+=1
        if s[i][j]+s[i+1][j+1]+s[i+2][j+2]+s[i+3][j+3]=='SAMX':t+=1
        if s[i+3][j]+s[i+2][j+1]+s[i+1][j+2]+s[i][j+3]=='XMAS':t+=1
        if s[i+3][j]+s[i+2][j+1]+s[i+1][j+2]+s[i][j+3]=='SAMX':t+=1
print(t)

h=len(s)
w=len(s[0])
t=0
for i in range(h-2):
    for j in range(w-2):
        if s[i+1][j+1]=='A':
            if s[i][j+2]+s[j+2][i] in ('SM','MS'):
                if s[i+2][j+2]+s[i][j] in ('SM','MS'):t+=1
print(t)
