import sys
import math
N,K = map(int,sys.stdin.readline().split())

if(N<=K):
    print("minigimbob")
    exit()
DP = [[] for i in range(K+1)]

DP[1].append(0)
DP[1].append(1)

visit = [False for i in range(N+1)]

for i in range(2,K+1):
    for num in DP[i-1]:
        cal_1 = num+1
        cal_2 = num + num//2
        
        if(cal_1 == N or cal_2 ==N):
            print("minigimbob")
            exit()
        if(cal_1<=N):
            if(not visit[cal_1]):
                DP[i].append(cal_1)
            visit[cal_1] = True
        if(cal_2<=N): 
            if(not visit[cal_2]):
                DP[i].append(cal_2)
            visit[cal_2] = True
        
print("water")


        