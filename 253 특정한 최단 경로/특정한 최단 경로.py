import sys
import heapq

def dijkstra(graph,start):
    distance = {node : float('inf') for node in graph.keys()}
    distance[start] = 0
    q = []
    heapq.heappush(q,(distance[start],start))
    
    while(q):
        cur_dist,cur_node = q.pop()
        
        if(cur_dist>distance[cur_node]):
            continue
        
        for node,now_dist in graph[cur_node].items():
            dist = cur_dist+now_dist
            if(distance[node]>dist):
                distance[node] = dist
                heapq.heappush(q,(dist,node))
    
    return distance
                
    
N,E = map(int,sys.stdin.readline().split())

graph = {i : {} for i in range(1,N+1)}

for i in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c
        
v1,v2 = map(int,sys.stdin.readline().split())

distance_0 = dijkstra(graph,1)
distance_1 = dijkstra(graph,v1)
distance_2 = dijkstra(graph,v2)

dist_1 = distance_0[v1]+distance_1[v2]+distance_2[N]
dist_2 = distance_0[v2]+distance_2[v1]+distance_1[N]

ans = min(dist_1,dist_2,float('inf')) 

print(-1) if ans == float('inf') else print(ans)