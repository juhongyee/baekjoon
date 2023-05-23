import sys
class Graph:
    def __init__(self,vertices) -> None:
        self.V = vertices
        self.graph = []
        
    def add_edge(self,edge):
        self.graph.append(edge)
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        
        return self.find(parent,parent[i]) #자기 자신을 root로 갖는 노드가 나올 때까지 탐색

    def union(self, parent, rank, x, y):
        x_root = self.find(parent,x)
        y_root = self.find(parent,y)
        
        #rank 자신을 root로 하는 subtree의 최대 크기.
        #처음엔 자기 자신을 rank로 가짐. rank가 큰 root에 붙이므로 cycle이 안 생김
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root #x_root를 y_root에 붙임.
        
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        
        else:
            parent[y_root] = x_root
            rank[x_root] += 1 #지금 현재 가지고 있는 최대 크기
    
    def kruskal(self):
        result = []
        i = 0
        e = 0
        
        self.graph = sorted(self.graph, key=lambda x : x[2])
        
        parent = []
        rank = []
        
        for node in range(self.V+1):
            parent.append(node) #자신의 부모를 자기 자신으로 초기화 parent = [i for i in range(self.V)]로 써도 됨.
            rank.append(0)
        
        while e<self.V-1:
            src, dest, weight = self.graph[i]
            i += 1
            x = self.find(parent, src) # 어떤 간선의 시작 노드가 속해있는 tree의 root 찾음
            y = self.find(parent, dest)# 어떤 간선의 끝 노드가 속해있는 tree의 root 찾음
            
            
            if x!=y: #parent가 같으면 같은 tree에 이미 간선으로 연결되어 있고 cycle이 있다는 의미이므로 다르다는 것은 cycle이 없다는 뜻
                e+=1
                result.append([src,dest,weight])
                self.union(parent, rank, x,y)
        
        return result

V,E = map(int,input().split())
g = Graph(V)
for _ in range(E):
    g.add_edge(tuple(map(int,sys.stdin.readline().split())))

result = g.kruskal()

sumation = 0

for src, dest, weight in result:
    sumation += weight

print(sumation)