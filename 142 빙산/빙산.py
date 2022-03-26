import sys
from collections import deque
x = [1,0,-1,0]
y = [0,-1,0,1]
q = deque()

def bfs(x1,y1,visited,ice,N,M):
    q.appendleft((x1,y1))

    while(q):
        current = q.pop()

        for i in range(0,4):
            if(1<=current[0]+x[i]<=N and 1<=current[1]+y[i]<=M):
                if(not visited[current[0]+x[i]][current[1]+y[i]] and ice[current[0]+x[i]][current[1]+y[i]]):
                    visited[current[0]+x[i]][current[1]+y[i]] = 1
                    q.appendleft((current[0]+x[i],current[1]+y[i]))                

#행의 개수 N과 열의 개수 M
N,M = map(int,input().split())

ice = [[0 for i in range(M+1)] for j in range(N+1)]
ice[0] = [0 for i in range(M+1)]
MEMORY = deque()
for i in range(1,N+1):
    ice[i] = [0]+list(map(int,sys.stdin.readline().split()))
    for j in range(1,M+1):
        if(ice[i][j]):
            MEMORY.append((i,j))

count  = -1
DIVIDE = False
m_count = [[0 for i in range(M+1)] for j in range(N+1)]
for k in MEMORY:
    if(ice[k[0]][k[1]]!=0): #얼음이 있으면
        melt_count = 0      #주변에 바다 셀거임
        for i in range(0,4):#주변 돌리기
            if(1<=k[0]+x[i]<=N and 1<=k[1]+y[i]<=M):
                if(ice[k[0]+x[i]][k[1]+y[i]]==0):
                    melt_count += 1
        m_count[k[0]][k[1]] = melt_count

while(not DIVIDE):
    #print(ice)
    count += 1
    area = 0
    
    if(count != 0):
        melted = deque()
        for k in MEMORY:
            if(ice[k[0]][k[1]]-m_count[k[0]][k[1]]>0):
                ice[k[0]][k[1]] -= m_count[k[0]][k[1]]
            else:
                if(ice[k[0]][k[1]] != 0):#0이 아니었다가 0으로 바뀐 순간에 넣어줘야 함.
                    melted.append((k[0],k[1]))
                ice[k[0]][k[1]] = 0
                
        while(melted):
            k = melted.pop()
            m_count[k[0]][k[1]] = 0
            for i in range(0,4):
                nx = k[0]+x[i]
                ny = k[1]+y[i]
                if(1<=nx<=N and 1<=ny<=M and ice[nx][ny]):
                    m_count[nx][ny] += 1
    
    #빙하가 나누어졌는지 check

    visited2 = [[0 for i in range(M+1)] for j in range(N+1)]
    count2 = 0 #빙하가 남았는지 확인
    for k in MEMORY:
        if(visited2[k[0]][k[1]] == 0 and ice[k[0]][k[1]] != 0):
            count2 += 1
            if(area==1):#이전에 이미 1개가 나왔었음. 그런데 발견이면 나누어짐
                DIVIDE = True
                print(count)
                sys.exit()
            visited2[k[0]][k[1]] = 1
            bfs(k[0],k[1],visited2,ice,N,M)
            area += 1

    if(count2==0):
        print(0)
        sys.exit()

