import sys
sys.setrecursionlimit(100000)

def union_find(n):
    parent = list(range(n))
    rank = [0]*n
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        
        return parent[x]
    
    def union(x,y):
        x_root = find(x)
        y_root = find(y)
        
        if x_root != y_root:
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root #rank가 더 높은 root에 붙이기
                
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
                
            else:
                parent[x_root] = y_root
                rank[x_root] += 1
    
    return find, union

n,m = map(int,sys.stdin.readline().split())

find,union = union_find(n+1)

for i in range(m):
    c,a,b = map(int,sys.stdin.readline().split())
    
    if(c==0):
        union(a,b)
    
    if(c==1):
        a_root = find(a)
        b_root = find(b)
        
        if(a_root==b_root):
            print("YES")
        else:
            print("NO")