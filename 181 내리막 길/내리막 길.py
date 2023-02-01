import sys

sys.setrecursionlimit(100000)

move =[(1,0),(-1,0),(0,-1),(0,1)] #하상좌우
#dfs를 재귀로 짜서 방문하지 않은 지점에서 최단거리를 구하고 방문한 지점은 그 값을 그냥 쓰자.
#dfs + dp
def dfs(x,y):
    global M
    global N
    global check
    global mapping


    if(check[x][y] == -1):
        check[x][y] = 0
        for i in range(0,4):
            x_2 = x + move[i][0]
            y_2 = y + move[i][1]
            
            if M>x_2>=0 and N>y_2>=0 and mapping[x][y]>mapping[x_2][y_2]:
                dfs(x_2,y_2)
                check[x][y]+=check[x_2][y_2]
    else:
        return

    
M,N = map(int,input().split())
check = [[-1 for i in range(N)] for j in range(M)]
mapping = [0 for i in range(M)]
for i in range(M):
    mapping[i] = list(map(int,sys.stdin.readline().split()))
check[M-1][N-1] = 1
dfs(0,0)

print(check[0][0])