import sys
sys.setrecursionlimit(50000)

def unionfind(n):
    parent = list(range(n))
    rank = [0]*n

    def find(x):
        if x!=parent[x]:
            parent[x] = find(parent[x])
        
        return parent[x]
    
    def union(x,y):
        x_root = find(x)
        y_root = find(y)
        
        if x_root != y_root:
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
                
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            
            else:
                parent[x_root] = y_root
                rank[x_root] += 1
            
            return False
            
        else:
            return True
    
    return find,union

n,m = map(int,sys.stdin.readline().split())

find,union = unionfind(n)

for i in range(m):
    A,B = map(int,sys.stdin.readline().split())
    if(union(A,B)):
        print(i+1)
        break
    
    if(i==m-1):
        print(0)
    