import sys
import math

N,M = map(int,input().split())

P = [0]+list(map(int,sys.stdin.readline().split()))
X = [0]+list(map(int,sys.stdin.readline().split()))

def greedy(i):
    j = 1
    count = 0
    while(1):
        cnt = P[i]
        dist = X[i]
        select = 0
        maximum = -1
        
        if(M<=cnt+dist):
            print(count)
            exit()
        #조건문의 앞에 쓰면 먼저 확인한다는 사실을 알게 됨.(앞에서부터 차례대로 확인하다가 끊음.)
        while(i+j<=N and P[i+j]<=cnt+dist):
            if maximum < P[i+j]+X[i+j] and cnt+dist<P[i+j]+X[i+j]:
                maximum = P[i+j]+X[i+j]
                select = i+j
            j += 1
                
        if(select != 0):
            i = select
            j = 1
            count += 1
        else:
            break

greedy(1)
print(-1)