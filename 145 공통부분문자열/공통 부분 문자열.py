#문자열 입력
A = input()
B = input()

A = '0'+A
B = '0'+B

lenA = len(A)
lenB = len(B)
MAX = 0
dp = [[0 for i in range(lenB+1)] for j in range(lenA+1)]

for i in range(1,lenA):
    for j in range(1,lenB):
        if(A[i] == B[j]):
            dp[i][j] = dp[i-1][j-1]+1
            if(dp[i][j]>MAX):
                MAX = dp[i][j]
        else:
            dp[i][j] = 0

#print(dp)
print(MAX)

        

