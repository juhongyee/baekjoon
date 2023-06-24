import sys
from collections import deque
import heapq

N,K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

deck_list = [deque() for _ in range(K+1)]

in_list = [False for i in range(K+1)]
ans = 0
heap = []
count = 0

# 경우
# 1. Hit -> 가장 뒤의 원소 바꿔주어야 함.
# 2. MISS N이 안참 -> list에 넣어(heap에 넣고,count증가시키고
# 3. MISS inf가 나왔다 -> 뒤에 원소가 없다.
#
#arr traverse
for idx,val in enumerate(arr):
    deck_list[val].append(idx)

for idx,val in enumerate(arr):
    deck_list[val].popleft()
    
    if(in_list[val]): #Hit
        if(deck_list[val]):#deck이 있다면
            heapq.heappush(heap,(-1*deck_list[val][0],val))
        else: #deck이 없다 <=> 뒤에 사용할 일이 없다.항상 튀어나와야 한다.
            heapq.heappush(heap,(-float('inf'),val))
        continue
    
    #if miss
    if(count<N): #not full
        in_list[val] = True
        if(deck_list[val]):#deck이 있다면
            heapq.heappush(heap,(-1*deck_list[val][0],val))
        else: #deck이 없다 <=> 뒤에 사용할 일이 없다.항상 튀어나와야 한다.
            heapq.heappush(heap,(-float('inf'),val))
        count += 1
        continue
    
    ans += 1
    #if full
    while heap:
        far_idx,far_val = heapq.heappop(heap)
        far_idx = -1*far_idx

        if(not deck_list[far_val]):
            if(far_idx == float('inf')):
               break
        else:
            if (deck_list[far_val][0]==far_idx):
                break
    
    #빼고 넣고
    in_list[far_val] = False
    in_list[val] = True
    
    if(deck_list[val]):#deck이 있다면
        heapq.heappush(heap,(-1*deck_list[val][0],val))
    else: #deck이 없다 <=> 뒤에 사용할 일이 없다.항상 튀어나와야 한다.
        heapq.heappush(heap,(-float('inf'),val))

print(ans)
        
    