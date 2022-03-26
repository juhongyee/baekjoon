#계단의 개수N
N = int(input())

stare = []
dp = [0 for i in range(N+1)]

for i in range(N):
    stare.append(int(input()))

dp[1] = stare[0]
if(N>=2):
    dp[2] = stare[0]+stare[1]
for i in range(3,N+1):
    dp[i] = max(dp[i-2]+stare[i-1],dp[i-3]+stare[i-2]+stare[i-1])

print(dp[N])
