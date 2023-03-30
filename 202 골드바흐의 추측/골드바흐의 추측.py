import sys

def sieve():
    erato = [1]*1000001
    
    erato[2] = 1
    
    for i in range(2,1000001):
        if(erato[i]==1):
            for j in range(i*2,1000001,i):
                erato[j] = 0

    return erato

#에라토스테네스의 체
erato = sieve()

n = int(sys.stdin.readline())

while(n!=0):
    for i in range(2,1000001):
        if(erato[i]==1):
            if(erato[n-i]==1):
                print("{} = {} + {}".format(n,i,n-i))
                break

    n = int(sys.stdin.readline())