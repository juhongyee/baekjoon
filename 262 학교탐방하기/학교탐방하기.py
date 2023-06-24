import heapq
import sys

N,M = map(int,sys.stdin.readline().split())

graph_1 = {}
graph_2 = {}
for i in range(M+1):
    A,B,C = map(int,sys.stdin.readline().split())
    
    if C==0:
        C = 1
    else:
        C = 0
        
    if A not in graph_1.keys():
        graph_1[A] = {B : C}
        graph_2[A] = {B : -C}
    else:
        graph_1[A][B] = C
        graph_2[A][B] = -C
        
    if B not in graph_1.keys():
        graph_1[B] = {A : C}
        graph_2[B] = {A : -C}
    else:
        graph_1[B][A] = C
        graph_2[B][A] = -C

def prim(graph:dict):
    heap = [(0,0)]
    connected = [False]*(N+1)
    sum_edge = 0
    
    while(heap):
        weight, v = heapq.heappop(heap)
        
        if not connected[v]:
            connected[v] = True
            sum_edge += weight
            
            for key,val in graph[v].items():
                if not connected[key]:
                    heapq.heappush(heap,(val,key))
    
    return sum_edge

print(abs(prim(graph_1)**2-prim(graph_2)**2))