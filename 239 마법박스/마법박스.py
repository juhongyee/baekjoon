import sys
N = int(input())
sieve = [1]*(N+1)

def binary(start,end,arr):
    if(start==end):
        print("! "+str(arr[start]))
        sys.stdout.flush()
        exit()
        
    Q = (start+end)//2
    
    print('? '+str(arr[Q]))
    sys.stdout.flush()
    
    ans = int(sys.stdin.readline())
    
    if(ans):
        binary(Q+1,end,arr)
    else:
        binary(start,Q,arr)

def recursive(start,end):
    Q = int(end**(1/2))
    
    if(Q<=start):
        for i in range(start,end+1):
            if(sieve[i]==1):
                print('? '+str(i))
                sys.stdout.flush()
                
                ans = int(sys.stdin.readline())
                if(ans==1):
                    for j in range(i+i,end+1,i):
                        sieve[j] = 0
                    sieve[i] = 0
                else:
                    print("! "+str(i))
                    sys.stdout.flush()
                    exit()
    
    #question
    print('? '+str(Q))
    sys.stdout.flush()
    
    ans = int(sys.stdin.readline())
    if(ans):
        prime_list = []
        #만약 작은게 다 있으면 그 위는 소수만 남음
        for i in range(start,Q+1):
            if(sieve[i]==1):
                for j in range(i+i,N+1,i):
                    sieve[j] = 0
                sieve[i] = 0
        for i in range(Q,end+1):
            if(sieve[i]==1):
                prime_list.append(i)
        
        binary(0,len(prime_list)-1,prime_list)
                
    else:
        recursive(start,Q)
        
recursive(2,N)