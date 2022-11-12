import sys
from collections import deque
#test case의 수
move = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
test = int(input())

for i in range(test):
    I = int(sys.stdin.readline())
    f_knight = list(map(int,sys.stdin.readline().split()))
    t_knight = list(map(int,sys.stdin.readline().split()))
    
    chess = [[0 for i in range(I)] for j in range(I)]
    queue = deque()
    count = 0
    queue.append(tuple(f_knight))
    #chess판에 이동횟수 기록
    chess[f_knight[0]][f_knight[1]] = 0
    fin = 0
    #bfs
    while queue:
        if(fin == 1):
            break
        #pop
        node = queue.popleft()
        
        for m in move:
            #chess판에 들어가면
            if(I-1>=node[0]+m[0]>=0 and I-1>=node[1]+m[1]>=0):
                #방문x이면                
                if(chess[node[0]+m[0]][node[1]+m[1]]==0):
                    if(t_knight[0] == node[0]+m[0] and t_knight[1] == node[1]+m[1]):
                        chess[node[0]+m[0]][node[1]+m[1]] = chess[node[0]][node[1]]+1
                        fin = 1
                        break
                    else:
                        queue.append((node[0]+m[0],node[1]+m[1]))
                        chess[node[0]+m[0]][node[1]+m[1]] = chess[node[0]][node[1]]+1
            
        
    if(f_knight[0] == t_knight[0] and f_knight[1] == t_knight[1]):
        print(0)
    else:
        print(chess[t_knight[0]][t_knight[1]])
        
        
    
    
    
    