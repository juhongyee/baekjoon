import sys
from collections import deque
import math

move = [(1,0),(-1,0),(0,1),(0,-1)] #상하우좌

def bfs(start,end,iter):
    global queue,visited,mapping,N,M
    
    while(queue):
        cnt = queue.popleft()
        
        for i in range(4):
            x = cnt[0]+move[i][0]
            y = cnt[1]+move[i][1]
            
            if(N>=x>=1 and M>=y>=1): #범위 안에 들어오면
                if(visited[x][y][iter]==-1): #이번 회차에 방문한 적이 없으면
                    if(mapping[x][y]!=1):
                        queue.append((x,y))
                        visited[x][y][iter] = visited[cnt[0]][cnt[1]][iter]+1
                    else:#1이면 queue에는 안 넣음.
                        visited[x][y][iter] = visited[cnt[0]][cnt[1]][iter]+1
                    
            
            
        

N,M = map(int,input().split())

mapping = [[0 for j in range(M+1)] for i in range(N+1)]

for i in range(1,N+1):
    temp = sys.stdin.readline().rstrip('\n')
    for j in range(1,len(temp)+1):
        mapping[i][j] = int(temp[j-1])

visited = [[[-1,-1] for j in range(M+1)] for i in range(N+1)]
visited[1][1] = [1,-1]
visited[N][M] = [-1,1]
queue = deque()

queue.append((1,1))
bfs(1,1,0)
queue.append((N,M))
bfs(N,M,1)

minimum = math.inf

for i in range(1,N+1):
    for j in range(1,M+1):
        if(mapping[i][j]==1):
            if(visited[i][j][0] != -1 and visited[i][j][1] != -1):
                if(minimum>sum(visited[i][j])-1):
                    minimum = sum(visited[i][j])-1

if(minimum>visited[1][1][1] and visited[1][1][1]!=-1):
    minimum = visited[1][1][1]
if(minimum == math.inf):
    print(-1)
else:
    print(minimum)