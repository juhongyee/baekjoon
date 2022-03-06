import sys

A = sys.stdin.readline().strip()
dp = [0 for i in range(len(A))]

count = 0

#initialize
if(A[0] != '0'):
    dp[0] = 1

if(len(A)>1):
    if(A[0] != '0'):
        if(A[1] != '0' and int(A[0]+A[1])<=26):
            dp[1] = 2

        elif(A[1] != '0'):
            dp[1] = 1

        elif(int(A[0]+A[1])<=26):
            dp[1] = 1

        else:
            dp[1] = 0
    else:
        dp[1] = 0

    for i in range(2,len(A)):
        if(A[i-1] != '0'):
            if(A[i] != '0' and int(A[i-1]+A[i])<=26):
                dp[i] = (dp[i-1]+dp[i-2])%1000000

            elif(A[i] != '0'):
                dp[i] = dp[i-1]

            elif(int(A[i-1]+A[i])<=26):
                dp[i] = dp[i-2]

            else:
                dp[i] = 0
        else:
            if(A[i] != '0'):
                dp[i] = dp[i-1]
            else:
                dp[i] = 0

        #print(i,dp[i])

print(dp[len(A)-1])
