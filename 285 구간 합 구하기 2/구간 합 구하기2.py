import sys

N,M,K = map(int,sys.stdin.readline().split())
tree = [[0,0] for i in range(4*N)]
arr = [0]

for i in range(N):
    arr.append(int(sys.stdin.readline()))
    
def init(node,left,right):
    if left == right:
        tree[node][0] = arr[left]
        return tree[node][0]
    else:
        mid = (left+right)//2
        tree[node][0] = init(node*2,left,mid)+init(node*2+1,mid+1,right)
        
        return tree[node][0]

def propagation(node,left,right):
    if left != right:
        tree[node*2][1] += tree[node][1] #몇을 update했는지 보내줘
        tree[node*2+1][1] += tree[node][1]
    
    tree[node][0] += tree[node][1] * (right-left+1)
    
    #Lazy clear
    tree[node][1] = 0

def update(node,left,right,start,end,value):
    propagation(node,left,right)
    
    if end<left or right<start:
        return
    
    if start<= left and right <= end:
        tree[node][0] += (right-left+1)*value
        
        if left != right:
            tree[node*2][1] += value
            tree[node*2+1][1] += value
        
        return
    
    mid = (left+right)//2
    update(node*2,left,mid,start,end,value)
    update(node*2+1,mid+1,right,start,end,value)
    tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
    
def query(node,left,right,start,end):
    propagation(node,left,right)
    
    if right < start or end <left:
        return 0
    
    if start <= left and right <= end:
        return tree[node][0]
    
    mid = (left+right)//2
    
    return query(node*2,left,mid,start,end) + query(node*2+1,mid+1,right,start,end)

init(1,1,N)
for i in range(M+K):
    q = list(map(int,sys.stdin.readline().split()))
    
    if q[0] == 1:
        update(1,1,N,q[1],q[2],q[3])
    
    elif q[0] == 2:
        print(query(1,1,N,q[1],q[2]))