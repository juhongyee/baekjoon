Check = {0 : 1}

def recur(N,P,Q):
    if(N//P in Check):
        r1 = Check.get(N//P)
    else:
        r1 = recur(N//P,P,Q)
        Check[N//P] = r1
        
    if(N//Q in Check):
        r2 = Check.get(N//Q)
    else:
        r2 = recur(N//Q,P,Q)
        Check[N//Q] = r2
    
    return r1+r2

N,P,Q = map(int,input().split())
if(N==0):
    print(1)
else:
    print(recur(N,P,Q))