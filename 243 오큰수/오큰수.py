import sys

N = int(input())

A = list(map(int,sys.stdin.readline().split()))

B = [0 for i in range(N)]

B[N-1] = (-1,-1)

for i in range(N-2,-1,-1):
    if(A[i]<A[i+1]):
        B[i] = (A[i+1],i+1)
    else:
        check = B[i+1]
        while(A[i]>=check[0] and not check[0] == -1):
            check = B[check[1]]
        
        B[i] = check

for idx,val in enumerate(B):
    print(val[0],end=' ')