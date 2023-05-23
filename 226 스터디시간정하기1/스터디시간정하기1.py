import sys
from collections import deque
N,T = map(int,sys.stdin.readline().split())

imos = [0]*100001

max_end = -1
for _ in range(N):
    K = int(sys.stdin.readline())
    for __ in range(K):
        start,end = map(int,sys.stdin.readline().split())
        imos[start] += 1
        imos[end] -= 1
        if(end>max_end):
            max_end = end

now = 0
for i in range(max_end+1):
    now += imos[i]
    imos[i] = now

queue = deque(imos[:T])
sumation = sum(queue)
cal = sumation
start = 0
end = T

for i in range(1,max_end+2-T):
    cal -= queue.popleft()
    queue.append(imos[T+i-1])
    cal += imos[T+i-1]
    
    if(sumation<cal):
        sumation = cal
        start = i
        end = i+T

print(start,end)

