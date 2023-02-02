import sys
import math
from collections import deque

move = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
#위 아래 상 하 우 좌

N,M,H = map(int,input().split())

tomato = [[0 for k in range(M)] for j in range(H)]
#h번째 높이 상자에서 M,N

for i in range(H):
    for j in range(M):
        tomato[i][j] = list(map(int,sys.stdin.readline().split()))

visited = [[[-1 for i in range(N)] for k in range(M)] for j in range(H)]
tomato_list = []
for i in range(H):
    for j in range(M):
        for k in range(N):
            if(tomato[i][j][k]==1 or tomato[i][j][k]==-1):
                visited[i][j][k] = 0
                if(tomato[i][j][k]==1):
                    tomato_list.append((i,j,k))

                    
def bfs():
    global visited,tomato,N,M,H
    global queue
    
    while(queue):
        item = queue.popleft()
        z = item[0]
        x = item[1]
        y = item[2]
        
        for i in range(6):
            z_2 = z+move[i][0]
            x_2 = x+move[i][1]
            y_2 = y+move[i][2]
            
            if(H>z_2>=0 and M>x_2>=0 and N>y_2>=0):
                if(visited[z_2][x_2][y_2] == -1):
                    tomato[z_2][x_2][y_2] = 1
                    visited[z_2][x_2][y_2] = visited[z][x][y] + 1
                    queue.append((z_2,x_2,y_2))

queue = deque()

for i in range(len(tomato_list)):
    z = tomato_list[i][0]
    x = tomato_list[i][1]
    y = tomato_list[i][2]
    
    queue.append((z,x,y))
    
bfs()

maximum = -math.inf
for i in range(H):
    for j in range(M):
        for k in range(N):
            if(tomato[i][j][k]==0):
                print(-1)
                exit()
            if(visited[i][j][k]>maximum):
                maximum = visited[i][j][k]
                
print(maximum)
