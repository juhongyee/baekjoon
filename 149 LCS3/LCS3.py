X = input()
Y = input()
Z = input()

lenX = len(X)
lenY = len(Y)
lenZ = len(Z)
X = '0'+X
Y = '0'+Y
Z = '0'+Z

dp = [[[0 for k in range(lenZ+1)] for i in range(lenY+1)] for j in range(lenX+1)]

for i in range(1,lenX+1):
    for j in range(1,lenY+1):
        for k in range(1,lenZ+1):
            if(X[i] == Y[j]==Z[k]):
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
                

print(dp[lenX][lenY][lenZ])