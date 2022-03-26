from collections import deque
import sys

sys.setrecursionlimit(99999)

x = [1,0,-1,0,1,1,-1,-1]
y = [0,-1,0,1,1,-1,1,-1]

def dfs(xs,ys,seum,visited,w,h):
        for i in range(0,8):
            if(1<=xs+x[i]<=h and 1<=ys+y[i]<=w):
                #print(xs+x[i],ys+y[i])
                if(seum[xs+x[i]][ys+y[i]]==1):
                    if(visited[xs+x[i]][ys+y[i]]!=1):
                        visited[xs+x[i]][ys+y[i]] = 1
                        dfs(xs+x[i],ys+y[i],seum,visited,w,h)
#높이와 너비
w,h = 1,1
while(1):
    w,h = map(int,sys.stdin.readline().split())
    if(w==0 and h==0):
        sys.exit()
    count = 0
    
    seummap = [[0 for i in range(w+1)] for j in range(h+1)]
    visited = [[0 for i in range(w+1)] for j in range(h+1)]
    for i in range(1,h+1):
        seummap[i] = [0]+list(map(int,sys.stdin.readline().split()))
        
    #print(seummap)
    for i in range(1,h+1):
        for j in range(1,w+1):
            if(visited[i][j] ==0 and seummap[i][j] == 1):
                count += 1
                visited[i][j] = 1
                dfs(i,j,seummap,visited,w,h)

    print(count)
