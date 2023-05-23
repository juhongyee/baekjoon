import sys

N = int(sys.stdin.readline())

consult = [[] for i in range(N+1)]
be_able = [[] for i in range(N+51)]

for i in range(1,N+1):
    day,cost = map(int,sys.stdin.readline().split())
    consult[i].append(day)
    consult[i].append(cost)
    
    be_able[i+day-1].append(i)

DP = [0 for i in range(N+1)]

for i in range(1,N+1):
    if(len(be_able[i])!=0):
        DP[i] = max(max([consult[able][1]+DP[able-1] for able in be_able[i]]),DP[i-1])
    else:
        DP[i] = DP[i-1]

print(DP[N])