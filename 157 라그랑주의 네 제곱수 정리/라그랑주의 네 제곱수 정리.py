import math

DP = [[0,0,0,0] for i in range(2**15+1)]

DP[1] = [1,0,0,0]
DP[2] = [0,1,0,0]
DP[3] = [0,0,1,0]

for i in range(4,2**15+1):
    for j in range(1,math.floor(math.sqrt(i))//2+1):
        if(j**2==i):
            DP[i][0] = 1
        DP[i][1] += DP[i-j**2][0]
        DP[i][2] += DP[i-j**2][1]
        DP[i][3] += DP[i-j**2][2]

while 1:
    a = int(input())
    if(not a):
        break
    else:
        sum = DP[a][0]+DP[a][1]+DP[a][2]+DP[a][3]
        print(sum)
