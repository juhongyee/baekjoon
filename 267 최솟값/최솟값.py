import sys

def sum_tree(tree,i):
    ans = 0
    while i>0 :
        ans += tree[i]
        i -= (i&-i)
    
    return ans

def update(tree,i,val):
    while i<len(tree):
        tree[i] += val
        i += (i&-i)

N,M = map(int,sys.stdin.readline().split())

tree = [0]*(N+1)
arr = [0]*(N+1)

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    if(a==0):
        if(b>c):
            temp = b
            b = c
            c = temp
        print(sum_tree(tree,c)-sum_tree(tree,b-1))
    else:
        update(tree,b,c-arr[b])
        arr[b] = c