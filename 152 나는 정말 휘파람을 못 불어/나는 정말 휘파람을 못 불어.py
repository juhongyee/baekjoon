import sys

mod = 1000000007

#문자열 길이 입력
N = int(input())

#문자열 입력
A = "0"+sys.stdin.readline()

#DP 선언 W,WH,WHE,WHEE의 개수
DP = [[0,0,0,0] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(4):
        DP[i][j] = DP[i-1][j]
        
    if(A[i] == 'W'):
        DP[i][0] = (DP[i][0]+1)%mod
        
    elif(A[i] == 'H'):
        DP[i][1] = (DP[i][1]+DP[i][0])%mod
    
    elif(A[i] == 'E'):
        DP[i][2] = (DP[i][2]+DP[i][1])%mod
        DP[i][3] = (2*DP[i][3]+DP[i-1][2])%mod #DP[i][2]가 앞줄에서 갱신되므로 얘만 바로 전 값을 가져오자.

print(DP[N][3])