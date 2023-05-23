import heapq
import sys
import math
from collections import deque

N = int(sys.stdin.readline())

def dijkstra(graph, start):
    distances = {node: [math.inf,0] for node in range(1,N+1)}
    distances[start] = [0,0]
    queue = []
    heapq.heappush(queue,[distances[start][0],start])
    
    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        #방문여부 check(if문이 만족한다면 더 작은 것이 이전에 나왔다는 의미(갱신하면 queue에 들어가므로) => 이미 방문했었음.)
        if distances[current_destination][0] < current_distance:
            continue
        
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination][0]:
                distances[new_destination][0] = distance
                distances[new_destination][1] = current_destination
                heapq.heappush(queue,[distance,new_destination])
    
    return distances

M = int(sys.stdin.readline())

graph = {node : {} for node in range(1,N+1)}

for i in range(M):
    depart,dest,cost = map(int,sys.stdin.readline().split())
    
    if dest not in graph[depart]:
        graph[depart][dest] = cost
    else:
        graph[depart][dest] = min(cost,graph[depart][dest])

start,end = map(int,sys.stdin.readline().split())

distances = dijkstra(graph,start)

q = deque()

back = end

q.append(end)

while back != start:
    q.append(distances[back][1])
    back = distances[back][1]

print(distances[end][0])
print(len(q))
for i in range(len(q)):
    print(q.pop(),end = ' ')