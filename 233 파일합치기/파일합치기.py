import sys

T = int(sys.stdin.readline())

for i in range(T):
    K = int(sys.stdin.readline())
    arr= list(map(int,sys.stdin.readline().split()))
    
    DP = [[float('inf') for i in range(K)] for j in range(K)]
    
    sub_sum = [arr[0]]
    for i in range(1,len(arr)):
        sub_sum.append(sub_sum[i-1]+arr[i])
    
    for size in range(1,K+1):
        for start in range(K):
            end = start+size-1

            if(end>K-1):
                continue
            if(end==start):
                DP[start][end] = 0
                
            for bar in range(start,end):
                DP[start][end] = min(DP[start][end],DP[start][bar]+DP[bar+1][end]+sub_sum[end]-sub_sum[start]+arr[start])
    
    print(DP[0][K-1])