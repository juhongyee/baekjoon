import sys
import math

C,N = map(int,input().split())

propa = [0]*N
for i in range(N):
    propa[i] = list(map(int,sys.stdin.readline().split()))

DP = [math.inf]*(C+101)
DP[0] = 0

for i in range(1,C+101):
    for j in range(N):
        if(i-propa[j][1]>=0):
            DP[i] = min(DP[i],DP[i-propa[j][1]]+propa[j][0])

print(min(DP[C:-1]))