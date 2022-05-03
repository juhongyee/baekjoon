
#물건종류의 수,최대 무게
N,M = map(int,input().split())

#물건의 무게,올라가는 만족도,물건의 개수
data = [[0,0,0] for i in range(N+1)]

for i in range(1,N+1):
    data[i] = list(map(int,input().split()))

dp = [[0 for i in range(M+1)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        #한 개의 무게보다도 현재의 담을 수 있는 무게가 작은 경우
        if(j<data[i][0]):
            dp[i][j] = dp[i-1][j]
        
        else:
            #최소 이 물건을 한 개는 담을 수 있는 경우
            dp[i][j] = dp[i-1][j]
            
            for k in range(1,data[i][2]+1):
                #k개의 무게합이 더 작은 경우
                if(j<k*data[i][0]):
                    break
                else:
                    if(dp[i-1][j-k*data[i][0]]+k*data[i][1]>dp[i][j]):
                        dp[i][j] = dp[i-1][j-k*data[i][0]]+k*data[i][1]
                    
print(dp[N][M])
                