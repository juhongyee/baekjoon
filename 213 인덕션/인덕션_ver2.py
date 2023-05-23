import sys
import math

N = int(sys.stdin.readline())

cuisine = [0]+list(map(int,sys.stdin.readline().split()))

DP = [[[[25000 for i in range(10)]for j in range(10)]for k in range(10)] for q in range(N+1)]

DP[0][0][0][0] = 0

for t in range(1,N+1):
    obj = cuisine[t]
    
    for i in range(10):
        for j in range(10):
            for k in range(10):
                DP[t][obj][j][k] = min(DP[t][obj][j][k],DP[t-1][i][j][k]+min((i-obj)%10,(obj-i)%10))
    
    for i in range(10):
        for j in range(10):
            for k in range(10):
                DP[t][i][obj][k] = min(DP[t][i][obj][k],DP[t-1][i][j][k]+min((j-obj)%10,(obj-j)%10))
    
    for i in range(10):
        for j in range(10):
            for k in range(10):
                DP[t][i][j][obj] = min(DP[t][i][j][obj],DP[t-1][i][j][k]+min((k-obj)%10,(obj-k)%10))
    
minimum = math.inf

for i in range(10):
    for j in range(10):
        for k in range(10):
            minimum = min(minimum,DP[N][i][j][k])

print(minimum)