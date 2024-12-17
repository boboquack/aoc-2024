A=INPUTA
B=INPUTB
C=INPUTC
prog=INPUTPROG

#A=SAMPLEA
#B=C=SAMPLEBC
#prog=SAMPLEPROG
prog=list(map(int,prog.split(',')))
def comb(i,A,B,C,prog):
    i=prog[i]
    if i<=3:return i
    if i==4:return A
    if i==5:return B
    if i==6:return C
    assert False
def run(A,B,C,prog):
    out=[]
    ip=0
    while 0<=ip<len(prog):
        match prog[ip]:
            case 0:
                A//=2**comb(ip+1,A,B,C,prog)
                ip+=2
            case 1:
                B^=prog[ip+1]
                ip+=2
            case 2:
                B=comb(ip+1,A,B,C,prog)%8
                ip+=2
            case 3:
                if A!=0:ip=prog[ip+1]
                else:ip+=2
            case 4:
                B^=C
                ip+=2
            case 5:
                out.append(comb(ip+1,A,B,C,prog)%8)
                ip+=2
            case 6:
                B=A//2**comb(ip+1,A,B,C,prog)
                ip+=2
            case 7:
                C=A//2**comb(ip+1,A,B,C,prog)
                ip+=2
    return out,A,B,C
print(','.join(str(i) for i in run(A,B,C,prog)[0]))

#for i in range(100):
#    print(oct(i),run(i,0,0,prog)[0])

cands=[0]
for p in range(len(prog)):
    lo=1 if p==0 else 0
    ncands=[]
    for ans in cands:
        for i in range(lo,8):
            if run(ans+i*8**(len(prog)-p-1),0,0,prog)[0][~p]==prog[~p]:
                ncands.append(ans+i*8**(len(prog)-p-1))
    cands=ncands
print(min(cands))

