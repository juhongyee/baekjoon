#정수 N
N = int(input())
if(N==1):
    print(0)
else:
    dp = [0 for i in range(N+1)]

    for i in range(2,N+1):
        if(i%3==0):
            if(i%2==0):
                dp[i] = min(dp[i//3],dp[i//2],dp[i-1])+1
            else:
                dp[i] = min(dp[i//3],dp[i-1])+1
        else:
            if(i%2==0):
                dp[i] = min(dp[i//2],dp[i-1])+1
            else:
                dp[i] = dp[i-1]+1

    print(dp[N])
