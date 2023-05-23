# import sys
# from collections import deque

# N,L = map(int,sys.stdin.readline().split())

# arr = list(map(int,sys.stdin.readline().split()))

# q = deque()

# for i in range(len(arr)):
    
#     while q and q[-1][0]>=arr[i]:
#         q.pop()
        
#     while q and q[0][1]<i-L+1:
#         q.popleft()
    
#     q.append((arr[i],i))
    
#     print(q[0][0],end = ' ')

#2번째 풀이
import sys
import heapq

N,L = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
arr_2 = []
i = 0

q = []

for i in range(len(arr)):
    if(i<L):
        heapq.heappush(q,(arr[i],i))
        print(q[0][0],end = ' ')
    else:
        heapq.heappush(q,(arr[i],i))
        while q[0][1]<i-L+1:
            heapq.heappop(q)
        print(q[0][0],end = ' ')

