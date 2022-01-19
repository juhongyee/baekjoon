import math

def sieve(n):
    erato = list(range(n+1))

    erato[0] = 0
    erato[1] = 1

    for k in range(2,math.floor(math.sqrt(n))+1):
        if(erato[k] == k):
            for j in range(2*k,n+1,k):
                if(erato[j]==j):
                    erato[j] = k#가장 작은 소인수
    return erato

def Chain(n):
    max_value = n
    sigma_value = [1 for i in range(max_value+1)]
    sumation = [1 for i in range(max_value+1)]
    min_fac = [1 for i in range(max_value+1)]
    erato = sieve(max_value)

    A = []
    for i in range(2,max_value+1):
        if(erato[i] == i):
            sigma_value[i] = i+1#일단 소수는 i+1로 초기화
        else:
            p = erato[i]
            m = i//p
            if(p != erato[m]):
                min_fac[i] = 1
            else:
                min_fac[i] = min_fac[m]+1

            c = min_fac[i]
            sigma_value[i] = int(sigma_value[m]*(math.pow(p,c+1)-1)/(math.pow(p,c)-1))#약수함수 sigma공식을 기반으로 짠 수식
        
        sumation[i] = sumation[i-1] + sigma_value[i]

    print(sigma_value[n])
    print(sumation[n])
    '''sumation = 0
    for k in range(1,n+1):
        sumation = sumation+sigma_value[k]
    print(sumation)'''
    '''for i in range(2,10001):
        k = prime_factor(i,erato)
        if(sigma_value[i] != k):
            print(i)
            print(k,sigma_value[i])'''
    '''print(sigma_value[7429])'''

def prime_factor(n,erato):

    if(n==1):
        return 1
    A = []
    B = []

    while(1):
        if(erato[n]==n):
            A.append(n)
            break
        else:
            A.append(erato[n])
            n = n//erato[n]
    
    for i in range(0,len(A)):
        B.append(A[i])

    B = list(set(B))
    sum1 = 1
    for i in range(0,len(B)):
        con = A.count(B[i])+1
        sum1 *= (B[i]**con-1)//(B[i]-1)

    return sum1

n = int(input())
erato = sieve(n)
sumation = 0

Chain(n)
