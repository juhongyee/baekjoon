import sys
sys.setrecursionlimit(10**6)
def PrintLCS(dp,X,i,j):
    if i == 0 or j==0:
        return
    if(dp[i][j][1] == 0):
        PrintLCS(dp,X,i-1,j-1)
        print(X[i],end = '')
    elif(dp[i][j][1] == 1):
        PrintLCS(dp,X,i-1,j)
    else:
        PrintLCS(dp,X,i,j-1)
        

X = input()
Y = input()

lenX = len(X)
lenY = len(Y)
X = '0'+X
Y = '0'+Y

dp = [[[0,0] for i in range(lenY+1)] for j in range(lenX+1)]

for i in range(1,lenX+1):
    for j in range(1,lenY+1):
        if(X[i] == Y[j]):
            dp[i][j][0] = dp[i-1][j-1][0]+1
        else:
            if(dp[i-1][j]>dp[i][j-1]):
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = 1
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1] = 2
                

print(dp[lenX][lenY][0])
x = lenX
y = lenY
PrintLCS(dp,X,x,y)