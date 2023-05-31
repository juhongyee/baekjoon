N = int(input())

prime = 9901

DP = [[0,0,0] for i in range(N+1)] #1번우리에 사자를 넣은 경우 #2번에 사자를 넣은 경우 #안 넣은 경우

DP[1][0] = 1
DP[1][1] = 1
DP[1][2] = 1

for i in range(2,N+1):
    DP[i][0] = (DP[i-1][1]+DP[i-1][2])%prime
    DP[i][1] = (DP[i-1][0]+DP[i-1][2])%prime
    DP[i][2] = (sum(DP[i-1]))%prime

print(sum(DP[N])%prime)