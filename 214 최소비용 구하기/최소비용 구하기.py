import heapq
import sys
import math

N = int(sys.stdin.readline())

def dijkstra(graph, start):
    distances = {node: math.inf for node in range(1,N+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[distances[start],start])
    
    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        #기존의 거리보다 길 수가 있음? 저 이전에 들어간 것
        #방문했었음.
        if distances[current_destination] < current_distance:
            continue
        
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
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

print(distances[end])