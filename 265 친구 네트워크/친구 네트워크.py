import sys
sys.setrecursionlimit(10**5)

def find(x,parent):
    if x!=parent[x]:
        parent[x] = find(parent[x],parent)
    
    return parent[x]

def union(x,y,parent,rank,num_set):
    x_root = find(x,parent)
    y_root = find(y,parent)
    
    if x_root != y_root:
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
            num_set[y_root] += num_set[x_root]
            print(num_set[y_root])
            
        elif rank[y_root] < rank[x_root]:
            parent[y_root] = x_root
            num_set[x_root] += num_set[y_root]
            print(num_set[x_root])
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
            num_set[x_root] += num_set[y_root]
            print(num_set[x_root])
    else:
        print(num_set[x_root])

N = int(input())

for i in range(N):
    M = int(input())
    name = {}
    parent = list(range(2*M))
    rank = [0]*(2*M)
    num_set = [1]*(2*M)
    
    for _ in range(M):
        A,B = sys.stdin.readline().split()
        
        if A not in name.keys():
            name[A] = len(name.keys())
        if B not in name.keys():
            name[B] = len(name.keys())
    
        num_A = name[A]
        num_B = name[B]
        
        union(num_A,num_B,parent,rank,num_set)