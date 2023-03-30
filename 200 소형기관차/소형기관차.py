import sys
import math

T = int(input())
train = [0]+list(map(int,sys.stdin.readline().split()))
N = int(input())

DP = [[0]*4 for i in range(T+1)]

#initialization
DP[N][1] = sum(train[1:N+1])
DP[2*N][2] = sum(train[N+1:2*N+1])
DP[3*N][3] = sum(train[2*N+1:3*N+1])

for i in range(N+1,T+1):
    new = sum(train[i-N+1:i+1])
    for j in range(1,4):
        DP[i][j] = max(DP[i-1][j],DP[i-N][j-1]+new)
        
print(DP[T][3])