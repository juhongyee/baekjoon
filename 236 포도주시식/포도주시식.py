import sys

n = int(sys.stdin.readline())

wine = [0 for i in range(n)]
DP = [[0,0,0] for i in range(n)]

for i in range(n):
    wine[i] = int(sys.stdin.readline())

for i in range(n):
    if(i==0):
        DP[0][1] = wine[0]
        continue
    elif(i==1):
        DP[1][0] = DP[0][1]
        DP[1][1] = wine[1]
        DP[1][2] = wine[0]+wine[1]
        continue

    DP[i][0] = max(DP[i-1])
    DP[i][1] = DP[i-1][0]+wine[i]
    DP[i][2] = DP[i-1][1]+wine[i]

print(max(DP[n-1]))
        