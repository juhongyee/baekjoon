import math
import sys
from collections import deque

#수빈이의 위치 N, 동생의 위치 K
N,K = map(int,input().split())

if(N==K):
    print(0)
    sys.exit(0)
    
gil = [[0,0] for i in range(100001)]

gil[N][0] = 1
gil[N][1] = 0
gil[K][0] = -1
gil[K][-1] = -1

queue = deque()
queue.appendleft([2*N,1])
queue.append([N+1,1])
queue.append([N-1,1])

minimum = math.inf
route = []
while(len(queue)!=0):

    temp = queue.pop()

    if(temp[0]>100000 or temp[0]<0):
        continue
    if(gil[temp[0]][0] == -1):
        if(minimum>temp[1]):
            minimum = temp[1]
            gil[temp[0]][1] = temp[1]
    if(gil[temp[0]][0] == 0):
        gil[temp[0]][0] = 1
        gil[temp[0]][1] = temp[1]
        queue.appendleft([2*temp[0],temp[1]+1])
        queue.appendleft([temp[0]+1,temp[1]+1])
        queue.appendleft([temp[0]-1,temp[1]+1])
    else:
        continue

print(minimum)

temp = minimum
place = K
route = []
while(temp!=-1):
    route.append(place)
    if(place%2==0 and gil[place//2][1] == temp-1):
        place = place//2
        temp -=1
    elif(gil[place+1][1] == temp-1):
        place = place+1
        temp -= 1
    elif(gil[place-1][1] == temp-1):
        place = place-1
        temp -= 1
print(route)
