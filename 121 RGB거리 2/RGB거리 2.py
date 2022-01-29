import math
#main idea : 첫번째 집을 3가지 경우로 나눠 모든 경우를 살펴본다.

def calculate_distace(dp,house,num):
    dp[1][0] = house[0][num]+house[1][0]
    dp[1][1] = house[0][num]+house[1][1]
    dp[1][2] = house[0][num]+house[1][2]

    dp[1][num] = math.inf

    n= len(dp)
    for i in range(2,n-1):
        dp[i][0] = min(dp[i-1][1]+house[i][0],dp[i-1][2]+house[i][0])
        dp[i][1] = min(dp[i-1][0]+house[i][1],dp[i-1][2]+house[i][1])
        dp[i][2] = min(dp[i-1][0]+house[i][2],dp[i-1][1]+house[i][2])

    minimum = math.inf
    
    for i in range(3):
        if(i!=num):
            if(i==0):
                dp[n-1][i] = min(dp[n-2][1]+house[n-1][0],dp[n-2][2]+house[n-1][0])
            elif(i==1):
                dp[n-1][i] = min(dp[n-2][0]+house[n-1][i],dp[n-2][2]+house[n-1][i])
            else:
                dp[n-1][i] = min(dp[n-2][0]+house[n-1][i],dp[n-2][1]+house[n-1][i])
        else:
            dp[n-1][i] = math.inf

        if(minimum>dp[n-1][i]):
            minimum=dp[n-1][i]

    return minimum

n = int(input()) #전체 집의 개수

house = [[] for j in range(n)]

for i in range(0,n):
    house[i] = list(map(int,input().split()))

dpR = [[0 for i in range(3)] for j in range(n)] #빨강 시작
dpG = [[0 for i in range(3)] for j in range(n)] #초록 시작
dpB = [[0 for i in range(3)] for j in range(n)] #파랑 시작

minimum = min(calculate_distace(dpR,house,0),calculate_distace(dpG,house,1),calculate_distace(dpB,house,2))
print(minimum)
