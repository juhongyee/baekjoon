from collections import deque
def Look_up_pretty(M):
    pretty = deque()
    for i in range(1,M+1):
        calcul = str(i)
        S = 0
        for j in range(len(calcul)):
            S += int(calcul[j])
        if(i%S==0):
            pretty.append(i)
    return pretty

M,K = map(int,input().split())
pretty = Look_up_pretty(M)
len_p = len(pretty)

#동전문제
dp = [1 for i in range(M+1)]

for i in range(1,len_p):
    coin = pretty[i]
    for j in range(coin,M+1):
        dp[j] += dp[j-coin]
        dp[j] %= K
        
print(dp[M])
