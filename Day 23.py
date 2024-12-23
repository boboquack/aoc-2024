s=INPUT.split()
ss=SAMPLE.split()
adj={}
for i in s:
    j,k=i.split('-')
    if j in adj:adj[j].add(k)
    else:adj[j]={k}
    if k in adj:adj[k].add(j)
    else:adj[k]={j}

u=0
for i in adj:
    for j in adj[i]:
        for k in adj[i]:
            if i<j<k and k in adj[j] and 't' in (i[0],j[0],k[0]):
                u+=1
print(u)

b=0
for i in sorted(adj):
    clique=[i]
    base=[sorted([k for k in adj[i] if k>i],reverse=True)]
    while base:
        if not base[-1]:
            clique.pop()
            base.pop()
            continue
        x=base[-1].pop()
        clique.append(x)
        if len(clique)>b:
            n=clique[:]
            b=len(clique)
        base.append(sorted({*base[-1]}&{k for k in adj[x] if k>x},reverse=True))
print(','.join(n))
