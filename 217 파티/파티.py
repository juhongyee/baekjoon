import sys
import heapq

N,M,X = map(int,sys.stdin.readline().split())

def dijkstra(graph,start):
    distances = [float('inf') for i in range(N+1)]
    distances[start] = 0
    q = []
    heapq.heappush(q,(distances[start],start))
    
    while q:
        cur_distance,cur_dest = heapq.heappop(q)
        
        if cur_distance>distances[cur_dest]:
            continue
        
        for new_dest,new_distance in graph[cur_dest].items():
            distance = cur_distance+new_distance
            
            if(distance<distances[new_dest]):
                distances[new_dest] = distance
                heapq.heappush(q,(distances[new_dest],new_dest))
    
    return distances

graph = {node : {} for node in range(1,N+1)}

for i in range(M):
    depart,arrive,cost =  map(int,sys.stdin.readline().split())
    graph[depart][arrive] = cost

x_distance = dijkstra(graph,X)

maximum = -1

for i in range(1,N+1):
    distances = dijkstra(graph,i)
    
    maximum = max(maximum,x_distance[i]+distances[X])

print(maximum)