import math

def sieve(n):
    erato = list(range(n+1))
    
    erato[0] = 0
    erato[1] = 1
    for i in range(2,math.floor(math.sqrt(n))+1): #만약 소인수분해가 된다면 이 범위 내에 있음.
        if(erato[i]==i):
            for k in range(i+i,n+1,i):
                if(erato[k] == k):
                    erato[k] = i
    return erato

def calcul(erato,i,dic):
    k = i
    while(k != erato[k]):
        if erato[k] in dic.keys():
            dic[erato[k]] += 1
        else:
            dic[erato[k]] = 1
    
        k = k//erato[k]
        
    if k in dic.keys():
        dic[erato[k]] += 1
    else:
        dic[erato[k]] = 1        
    
    even = 0
    odd = 1
    
    for prime in dic.keys():
        if(prime==2):
            even = dic[prime]
        else:
            odd *= dic[prime]+1
    
    return even*odd-odd
    

S,T = map(int,input().split())

sumation = 0
erato_list = sieve(T+1)
for i in range(S,T+1):
    if(i==1):
        sumation += -1
    else:
        sumation += calcul(erato_list,i,{})
    
print(sumation)