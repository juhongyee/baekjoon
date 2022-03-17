import math
import sys
from collections import deque

#수빈이의 위치 N, 동생의 위치 K
N,K = map(int,input().split())

if(N==K):
    print(0)
    sys.exit(0)
    
gil = [0 for i in range(100001)]

gil[N] = 1
gil[K] = -1

queue = deque()
queue.append([2*N,0])
queue.appendleft([N-1,1])
queue.appendleft([N+1,1])


minimum = math.inf
while(len(queue)!=0):

    temp = queue.pop()

    if(temp[0]>100000 or temp[0]<0):
        continue
    if(gil[temp[0]] == -1):
        if(minimum>temp[1]):
            minimum = temp[1]
    if(gil[temp[0]] == 0):
        gil[temp[0]] = 1
        queue.append([2*temp[0],temp[1]])
        queue.appendleft([temp[0]-1,temp[1]+1])
        queue.appendleft([temp[0]+1,temp[1]+1])
    else:
        continue

print(minimum)
