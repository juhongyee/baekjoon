import sys

N,M = map(int,sys.stdin.readline().split())

clear_time = [0]*(N+1)
clear_time[0] = [0 for i in range(M)]

for i in range(1,N+1):
    clear_time[i] = list(map(int,sys.stdin.readline().split()))

dp = [[0 for i in range(M)] for j in range(N+1)]

for i in range(1,N+1):
    minimum = min(dp[i-1])
    min_idx = 0
    for j in range(M):
        if(dp[i-1][j] == minimum):
            min_idx = j
            break
    
    for j in range(M):
        if(min_idx != j):
            dp[i][j] = minimum + clear_time[i][j]
        else:
            min_2 = float('inf')
            for k in range(M):
                if(k==j):
                    continue
                min_2 = min(min_2,dp[i-1][k])
            dp[i][j] = min_2 + clear_time[i][j]

print(min(dp[N]))
            