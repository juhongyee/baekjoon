import sys
sys.setrecursionlimit(100000)
prime = 10**9+7

N,M = map(int,input().split())
a_1,b_1,c_1 = map(int,input().split())
a_2,b_2,c_2 = map(int,input().split())

agent = [[a_1,a_2],[b_1,b_2],[c_1,c_2]]

def square(N,M):
    if(M == 0):
        return 1
    if(M == 1):
        return N
    if(M == 2):
        return N**2
    
    if(M%2 == 0):
        return (square(N,M//2)**2)%prime
    else:
        return ((square(N,M//2)**2)*N)%prime

# print(recursive(-1,1,0))
#딱맞게 뭐가 된 경우
DP = [[[[0,0],[0,0],[0,0]] for i in range(M)]for j in range(M+1)]

#make initial


total = 0
for i in range(2,M+1):
    new_one  = 0
    for j in range(1,M):
        for k in range(3):
            for t in range(2):
                for a in range(3):
                    for b in range(2):
                        if(k==a):
                            if(j-agent[a][b]//2>=1):
                                DP[i][j][k][t] += DP[i-1][j-agent[k][t]//2][a][b]
                                DP[i][j][k][t] %= prime
                        else:
                            if(j-agent[a][b]>=1):
                                DP[i][j][k][t] += DP[i-1][j-agent[k][t]][a][b]
                                DP[i][j][k][t] %= prime
                                
for i in range(M):
    for j in range(3):
        total += sum(DP[i][M][j])*square(6,N-i)

print(total)
    
    

        

