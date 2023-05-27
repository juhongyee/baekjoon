import sys
from collections import deque

N,M,K = map(int,sys.stdin.readline().split())

arr = [[i+j for i in range(1,M+1)] for j in range(N)]

if(K<arr[N-1][M-1]):
    print("NO")
else:
    print("YES")
    for i in range(N):
        for j in range(M):
            print(arr[i][j],end=' ')
        print()