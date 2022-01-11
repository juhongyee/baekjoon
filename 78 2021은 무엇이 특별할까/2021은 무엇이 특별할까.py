import math

def cieve(n):
    erato = [1 for i in range(n+1)]

    erato[0] = 0
    erato[1] = 0

    for k in range(2,math.floor(math.sqrt(n))+1):
        if(erato[k] == 1):
            for j in range(2*k,n+1,k):
                erato[j] = 0

    return erato

def func():
    N = int(input())
    erato = cieve(20000)
    for k in range(N+1,20001):
        a = math.ceil(math.sqrt(k))

        for i in range(a,1,-1):
            if(erato[i]):
                for j in range(i+1,20001):
                    if(erato[j] == 1):
                        if(i*j == k):
                            print(k)
                            return 0
                        else:
                            break
                            
                    
            
func()
