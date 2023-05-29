import sys

prime = 10**9+9

DP = [[0,0,0] for i in range(100001)]

DP[1][0] = 1
DP[2][0] = 0
DP[2][1] = 1
DP[3][0] = 1
DP[3][1] = 1
DP[3][2] = 1

for i in range(4,100001):
    DP[i][0] = (DP[i-1][1]+DP[i-1][2])%prime
    DP[i][1] = (DP[i-2][0]+DP[i-2][2])%prime
    DP[i][2] = (DP[i-3][0]+DP[i-3][1])%prime

T = int(input())
for i in range(T):
    n = int(sys.stdin.readline())
    print(sum(DP[n])%prime)