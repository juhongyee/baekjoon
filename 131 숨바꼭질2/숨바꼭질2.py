import math
import sys
from collections import deque

#수빈이의 위치 N, 동생의 위치 K
N,K = map(int,input().split())

if(N==K):
    print(0)
    print(1)
    sys.exit(0)
    
gil = [[0,0] for i in range(100001)]

gil[N] = [1,0]
gil[K] = [-1,0]

queue = deque()
queue.appendleft([2*N,1])
queue.append([N+1,1])
queue.append([N-1,1])

minimum = [math.inf,0]
while(len(queue)!=0):

    temp = queue.pop()

    if(temp[0]>100000 or temp[0]<0):
        continue
    if(gil[temp[0]][0] == -1):
        if(minimum[0]>temp[1]):
            minimum[0] = temp[1]
            minimum[1] = 1
        elif(minimum[0]==temp[1]):
            minimum[1] = minimum[1]+1
    if(gil[temp[0]][0] == 0):
        gil[temp[0]][0] = 1
        gil[temp[0]][1] = temp[1]
        queue.appendleft([2*temp[0],temp[1]+1])
        queue.appendleft([temp[0]+1,temp[1]+1])
        queue.appendleft([temp[0]-1,temp[1]+1])
        
    elif(gil[temp[0]][1]==temp[1]):
        queue.appendleft([2*temp[0],temp[1]+1])
        queue.appendleft([temp[0]+1,temp[1]+1])
        queue.appendleft([temp[0]-1,temp[1]+1])
    else:
        continue

print(minimum[0])
print(minimum[1])
