import sys

def unionfind(n):
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
                parent[x_root] = y_root
            
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            
            else:
                rank[x_root] += 1
                parent[x_root] = y_root
                
    return find,union

N = int(input())
M = int(input())

find,union = unionfind(N+1)

for i in range(N):
    num = i+1
    
    connected = list(map(int,sys.stdin.readline().split()))
    for idx,check in enumerate(connected):
        if(check):
            union(num,idx+1)

plan = list(map(int,sys.stdin.readline().split()))

flag = True

for idx in range(M-1):
    root_1 = find(plan[idx])
    root_2 = find(plan[idx+1])
    
    if(root_1!=root_2):
        flag = False
        break
    
if(flag):
    print("YES")
else:
    print("NO")    