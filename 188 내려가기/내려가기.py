import sys

N = int(input())

dp = [0]

for i in range(N):
    if(i==0):
        dp[i] =list(map(int,sys.stdin.readline().split()))
        dp = [[dp[0][0],dp[0][0]],[dp[0][1],dp[0][1]],[dp[0][2],dp[0][2]]]
        dp_2 = [[0,0],[0,0],[0,0]]
    else:
        data =list(map(int,sys.stdin.readline().split()))
        for j in range(3):
            if(j==0):
                data[j] = [max(dp[0][0],dp[1][0])+data[j],min(dp[0][1],dp[1][1])+data[j]]
            elif(j==1):
                data[j] = [max(dp[0][0],dp[1][0],dp[2][0])+data[j],min(dp[0][1],dp[1][1],dp[2][1])+data[j]]
            else:
                data[j] = [max(dp[1][0],dp[2][0])+data[j],min(dp[1][1],dp[2][1])+data[j]]
        dp = data
            

maximum = dp[0][0]
minimum = dp[0][1]

for i in range(3):
    if(maximum<dp[i][0]):
        maximum = dp[i][0]
    if(minimum>dp[i][1]):
        minimum = dp[i][1]

print(maximum,minimum)