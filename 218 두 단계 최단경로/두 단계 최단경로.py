import sys
import heapq

N,M = map(int,sys.stdin.readline().split())

def dijkstra(graph,start,flag):
    distances = [float('inf') for i in range(N+1)]
    q = []
    distances[start] = 0
    heapq.heappush(q,(0,start))
    
    while q:
        cur_dist,cur_dest = heapq.heappop(q)
        
        if cur_dist>distances[cur_dest]:
            continue
            
        for new_dest,new_dist in graph[cur_dest].items():
            if(new_dest == flag):
                continue
            distance = new_dist+cur_dist
            if(distance<distances[new_dest]):
                distances[new_dest] = distance
                heapq.heappush(q,(distance,new_dest))
                
    return distances

graph = {i : {} for i in range(1,N+1)}

for _ in range(M):
    depart,arrive,cost = map(int,sys.stdin.readline().split())
    graph[depart][arrive] = cost

X,Y,Z = map(int,sys.stdin.readline().split())

distances_1 = dijkstra(graph,X,flag=Y)
distances_2 = dijkstra(graph,Y,flag=0)
distances_3 = dijkstra(graph,X,flag=0)

if(distances_1[Z] != float('inf')):
    if(distances_3[Y]+distances_2[Z] != float('inf')):
        print("{} {}".format(distances_3[Y]+distances_2[Z],distances_1[Z]))
    else:
        print("{} {}".format(-1,distances_1[Z]))

else:
    if(distances_3[Y]+distances_2[Z] != float('inf')):
        print("{} {}".format(distances_3[Y]+distances_2[Z],-1))
    
    else:
        print("{} {}".format(-1,-1))