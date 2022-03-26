import sys
from collections import deque 

x = [1,0,-1,0]
y = [0,-1,0,1]
q = deque()

def bfs(x1,y1,visited,A,N,count):
    q.appendleft((x1,y1))

    while(q):
        current = q.pop()
        for i in range(0,4):
            if(0<current[0]+x[i]<=N and 0<current[1]+y[i]<=N):
                if(not visited[current[0]+x[i]][current[1]+y[i]] and A[current[0]+x[i]][current[1]+y[i]]-count>0):
                    visited[current[0]+x[i]][current[1]+y[i]] = 1
                    q.appendleft((current[0]+x[i],current[1]+y[i]))


#행렬 size N입력

N = int(input())

A = [[] for i in range(N+1)]
A[0] = [0 for i in range(N+1)]

for i in range(1,N+1):
   A[i] = [0] + list(map(int,sys.stdin.readline().split()))
#print(A)
maximum = 0
AOS = 1
count = -1

while(AOS):
    AOS = 0
    count+=1
    visited = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if(A[i][j]-count>0 and visited[i][j] == 0):
                visited[i][j] = 1
                bfs(i,j,visited,A,N,count)
                AOS += 1
    del visited
    if(maximum<AOS):
        maximum = AOS

print(maximum)
        
