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

def prime_factor(n,erato):

    while(1):
        if(erato[n]==n):
            print(n)
            return 0
        else:
            print(erato[n],end=' ')
            n = n//erato[n]
    
n = input()
a = input()
a = a.split()

erato = sieve(5000000)

for i in range(0,len(a)):
    prime_factor(int(a[i]),erato)

    
