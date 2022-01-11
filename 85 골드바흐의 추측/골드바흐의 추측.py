import math

def sieve(n):
    erato = [1 for i in range(n+1)]

    erato[0] = 0
    erato[1] = 0

    for k in range(2,math.floor(math.sqrt(n))+1):
        if(erato[k] == 1):
            for j in range(2*k,n+1,k):
                erato[j] = 0

    return erato

erato = sieve(1000000)

while(1):
    a = int(input())

    if(a):
        for i in range(2,a+1):
            if((erato[i]==1) and (erato[a-i]==1)):
                print('%d = %d + %d'%(a,i,a-i))
                break

    else:
        break
