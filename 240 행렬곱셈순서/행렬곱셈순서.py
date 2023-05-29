#start x가 있다고 하자. x의 시작과 3x2 2x4 4x4, start의 0 bar의 1,end의1곱해서 더하기
import sys

N = int(input())

matrix = []

for i in range(N):
    matrix.append(tuple(map(int,sys.stdin.readline().split())))

DP = [[float('inf') for j in range(N)] for i in range(N)]

for i in range(N):
    DP[i][i] = 0

for size in range(2,N+1):
    for start in range(N):
        end = start+size-1
        if end<N:
            # 2 3 4 5 6
            for bar in range(start,end):
                DP[start][end] = min(DP[start][end],DP[start][bar]+DP[bar+1][end]+matrix[start][0]*matrix[bar][1]*matrix[end][1])

print(DP[0][N-1])