import sys
import heapq
N = int(input())

cost = []

for i in range(N):
    cost.append(list(map(int,sys.stdin.readline().split())))

cost.sort(key=lambda x:x[1])

ans = []

for val in cost:
    heapq.heappush(ans,val[0])
    if len(ans) > val[1]:
        heapq.heappop(ans)
print(sum(ans))