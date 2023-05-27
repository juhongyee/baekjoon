DP = [0 for i in range(12)]

DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4,12):
    DP[i] = DP[i-3]+DP[i-2]+DP[i-1]
    
T = int(input())

for i in range(T):
    print(DP[int(input())])