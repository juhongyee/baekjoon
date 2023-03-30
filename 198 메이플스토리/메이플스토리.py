import sys
import math
N,T = map(int,sys.stdin.readline().split())

time_for_moving = [0 for j in range(N)]
c = []
e = []

for i in range(N):
    c_0,e_0 = map(int,sys.stdin.readline().split())
    c.append(c_0)
    e.append(e_0)

for i in range(N):
    time_for_moving[i] = list(map(int,sys.stdin.readline().split()))

DP = [[0 for i in range(N)] for j in range(T+1)]

for i in range(N):
    if(c[i] != 0):
        DP[0][i] = -math.inf

for t in range(1,T+1):
    for i in range(N):
        DP[t][i] = DP[t-1][i]+e[i]
        for j in range(N):
            if(t-time_for_moving[j][i]>=0 and DP[t-time_for_moving[j][i]][j]>=c[i] and i!=j):
                DP[t][i] = max(DP[t][i],DP[t-time_for_moving[j][i]][j])

print(max(DP[T]))
