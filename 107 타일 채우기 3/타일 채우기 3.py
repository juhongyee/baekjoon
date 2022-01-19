#n번째 행의 n 입력
n = int(input())

case = [0 for i in range(n+1)]
dp = [1 for i in range(n+1)]
dp[0] = 1
dp[1] = 3

case[1] = 2
if(n>=2):
    case[2] = 7
    dp[2] = 10
if(n>=3):
    case[3] = 22
    dp[3] = 32

if(n<=3):
    print(case[n])

else:
    for i in range(4,n+1):
        case[i] = (case[i-1]*2+case[i-2]*3+dp[i-3]*2)%1000000007
        dp[i] = dp[i-1]+case[i]

    print(case[n])
