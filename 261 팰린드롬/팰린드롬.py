import sys

N = int(input())

arr = [0] + list(map(int,sys.stdin.readline().split()))

M  = int(input())

DP = [[0 for i in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    DP[i][i] = 1
    
for diff in range(1,N+1):
    for start in range(1,N+1):
        end = start+diff
        if(end>N):
            continue
        
        if(arr[start] == arr[end]):
            if(start+1<=end-1):
                if(DP[start+1][end-1]):
                    DP[start][end] = 1
            else:
                DP[start][end] = 1

for _ in range(M):
    S,E = map(int,sys.stdin.readline().split())
    print(DP[S][E])