s=INPUT.split('\n')
ss=SAMPLE.split('\n')
l=[]
for i in s:
    p,v=i.split()
    p=tuple(map(int,p[2:].split(',')))
    v=tuple(map(int,v[2:].split(',')))
    l.append((p,v))

tl,tr,bl,br=0,0,0,0
w,h=101,103
#w,h=11,7
for p,v in l:
    px,py=p
    vx,vy=v
    ox=(px+100*vx)%w
    oy=(py+100*vy)%h
    if ox<w//2:
        if oy<h//2:
            bl+=1
        elif oy>h//2:
            tl+=1
    elif ox>w//2:
        if oy<h//2:
            br+=1
        elif oy>h//2:
            tr+=1
print(tl*tr*bl*br)

off=[(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y)!=(0,0)]
u=[None]*(w*h)
for t in range(w*h):
    g=[[False]*w for i in range(h)]
    c=0
    for p,v in l:
        px,py=p
        vx,vy=v
        ox=(px+t*vx)%w
        oy=(py+t*vy)%h
        g[oy][ox]=True
    for p,v in l:
        px,py=p
        vx,vy=v
        ox=(px+t*vx)%w
        oy=(py+t*vy)%h
        c+=all(not g[(oy+dx)%h][(ox+dy)%w] for dx,dy in off)
    u[t]=c
z=min(u)
a=[i for i in range(w*h) if u[i]==128]
for t in a:
    g=[[False]*w for i in range(h)]
    c=0
    for p,v in l:
        px,py=p
        vx,vy=v
        ox=(px+t*vx)%w
        oy=(py+t*vy)%h
        g[oy][ox]=True
    for p,v in l:
        px,py=p
        vx,vy=v
        ox=(px+t*vx)%w
        oy=(py+t*vy)%h
        c+=all(not g[(oy+dx)%h][(ox+dy)%w] for dx,dy in off)
    u[t]=c
    print(t)
    for i in g:
        print(''.join('#' if j else '.' for j in i))
    print()
