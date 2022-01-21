import sys

class queue:
    def __init__(self):
        self.queue = [(0,0) for i in range(1000000)]
        self.front = -1
        self.rear = -1

    def empty(self):
        return self.front==self.rear

    def push(self,data):
        self.rear += 1
        self.queue[self.rear] = data

    def pop(self):
        if(self.empty()):
            return -1
        self.front += 1
        return self.queue[self.front]
#BFS
def BFS(a,b,q):
    new_x = 0
    new_y = 0
    visited[a][b] = 1
    for i in range(0,4):
        new_x = a+x[i]
        new_y = b+y[i]
        if(0<=new_x<=row-1 and 0<=new_y<=col-1):
            if(tomato[new_x][new_y]==0 and not visited[new_x][new_y]):
                #조건에 해당이 되면 방문하고 모두 queue에 넣음.
                visited[new_x][new_y] = 1
                q.push((new_x,new_y))
            
def day_conclusion(q1,q2):
    while(not q1.empty()):
        temp = q1.pop()
        #print(temp[0],temp[1])
        #if(not update[temp[0]][temp[1]]):#update를 한 적이 없으면
        BFS(temp[0],temp[1],q2)
        #update[temp[0]][temp[1]] = True

#행과 열을 받음.
global col,row
col,row = map(int,input().split())
day = 0 #결과적으로 얼마나 지났는지
complete = False #완료여부

#tomato는 격자판 저장
#update는 이 격자를 중심으로 주변을 갱신했는지 알아봄
#visited는 이 격자가 방문된 적이 있는지 파악
global tomato
global visited
tomato = [[0 for i in range(col)] for j in range(row)]
visited = [[0 for i in range(col)] for j in range(row)]
#update = [[0 for i in range(col)] for j in range(row)]

#클래스로 두 개의 queue를 만듦
q1 = queue()
q2 = queue()

#For BFS
global x
global y
x = (-1,0,1,0)
y = (0,-1,0,1)

#토마토 정보 입력
for i in range(0,row):
    #tomato입력,shallow copy 각 행에
    A = list(map(int,sys.stdin.readline().split()))
    tomato[i] = A
    
#queue intitialize,한 바퀴 돌며 1인 값들을 queue에 넣음.
for i in range(0,row):
    for j in range(0,col):
        if(tomato[i][j]==1):
            q1.push((i,j))

#홀수 날에는 q1에서 pop하여 q2에 넣고 짝수 날에는 q2에서 pop하여 q1에 넣음
#만약 다 넣었는데 queue에 아무 것도 들어 있지 않으면 완료
while(not complete):
    if(day%2==0):

        day_conclusion(q1,q2)
        if(q2.empty()):
            complete = True
            break
    else:
        day_conclusion(q2,q1)
        if(q1.empty()):
            complete = True
            break
    day += 1 #하루가 지남

#출력
for i in range(0,row):
    if(day==-1):
        break
    for j in range(0,col):
        if(not visited[i][j] and not (tomato[i][j]==-1)):
            day = -1
            break 
print(day)  
