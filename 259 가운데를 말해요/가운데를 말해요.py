import sys
import heapq

N = int(input())
A = int(sys.stdin.readline())
print(A)
upper = [] #min heap
lower = [-A] #max heap

# A가 들어왔을 때 양쪽의 개수가 동일하다고 하자. 혹은 lower가 한 개가 많은 상황
# 만약 upper[0]보다 A가 크면 upper에 넣고
# 작으면 lower에 넣는다.
# inital condition을 맞춰주고 뽑는다.

for i in range(2,N+1):
    A = int(sys.stdin.readline())
    
    if -lower[0]>=A:
        heapq.heappush(lower,-A)
    else:
        heapq.heappush(upper,A)
    
    if(upper and len(upper)>len(lower)):
        heapq.heappush(lower,-heapq.heappop(upper))
    elif(len(lower)-len(upper)==2):
        heapq.heappush(upper,-heapq.heappop(lower))
    print(-lower[0])
        