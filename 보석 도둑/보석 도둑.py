import sys
import heapq

N,K = map(int,sys.stdin.readline().split())

jewel = []
bag = []

#heap을 편하게 사용하기 위해 값을 앞에 둠.
for i in range(N):
    item1,item2 = map(int,sys.stdin.readline().split())
    item2 *= -1
    jewel.append((item2,item1))

for i in range(K):
    item = int(sys.stdin.readline())
    bag.append(item)

jewel.sort(key = lambda x:x[1])
bag.sort()

result = 0
i = 0
start = 0
heap = []
heapq.heapify(heap)

for val in bag:
    if(i<N):
        while(jewel[i][1]<=val):
            i += 1
            if(i==N):
                break
        
    #i가 갱신되면 새로 넣어지고 갱신되지 않으면 들어가지 않음.
    for j in range(start,i):
        heapq.heappush(heap,jewel[j][0])
    
    if(heap):
        result -= heapq.heappop(heap)
    start = i
    
print(result)
