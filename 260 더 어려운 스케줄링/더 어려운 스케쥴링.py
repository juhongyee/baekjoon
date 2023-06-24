import sys
from collections import deque
import heapq

pointer = True #True == front, False == Back
deck = deque()
min_heap = []
max_heap = []

N,Q = map(int,sys.stdin.readline().split())

finished = [0]*(N+1)
point_list = deque()
for i in range(Q):
    order = list(map(int,sys.stdin.readline().split()))

    #0
    if len(order) == 2:
        deck.appendleft(order[1])
    else:
        if(order[0] == 1):
            while(deck):
                val = deck.popleft()
                heapq.heappush(min_heap,val)
                heapq.heappush(max_heap,-val)
        
        elif(order[0] == 2):
            point_list.append(False if pointer else True)
        
        else:
            if(deck):
                if(pointer):
                    val = deck.popleft()
                    finished[val] = True
                    print(val)
                else:
                    if(max_heap):
                        while max_heap:
                            val = -heapq.heappop(max_heap)
                            if(finished[val]):
                                continue
                            else:
                                break
                        if(finished[val]):
                            val = deck.pop()
                            
                        finished[val] = True
                        print(val)
                    else:
                        val = deck.pop()
                        finished[val] = True
                        print(val)
            else:
                if(pointer):
                    while 1:
                        val = heapq.heappop(min_heap)
                        if(finished[val]):
                            continue
                        else:
                            break
                        
                    finished[val] = True
                    print(val)
                else:
                    while 1:
                        val = -heapq.heappop(max_heap)
                        if(finished[val]):
                            continue
                        else:
                            break
                    finished[val] = True
                    print(val)