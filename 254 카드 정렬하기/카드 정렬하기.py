import heapq
import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

heapq.heapify(arr)
ans = 0
while(len(arr)!=1):
    min_1 = heapq.heappop(arr)
    min_2 = heapq.heappop(arr)
    ans += (min_1+min_2)
    heapq.heappush(arr,min_1+min_2)

print(ans)
    