#diff_list인 B를 만들고 L,R에 각각 업데이터 되는 x만 더하고 빼주자.
import sys

def sum_tree(tree,i):
    ans = 0
    while i>0:
        ans += tree[i]
        i -= (i&-i)
    
    return ans

def update(tree,i,diff):
    while i<len(tree):
        tree[i] += diff
        i += (i&-i)

N = int(sys.stdin.readline())
A = [0]+list(map(int,sys.stdin.readline().split()))
B = [0]+[A[i]-A[i-1] for i in range(1,N+1)]

tree = [0]*(N+1)

M = int(input())

for i in range(1,N+1):
    update(tree,i,B[i])

for _ in range(M):
    quary = list(map(int,sys.stdin.readline().split()))
    
    if(len(quary)==4):
        i = quary[1]
        j = quary[2]
        k = quary[3]
        update(tree,i,k)
        if(j!=N):
            update(tree,j+1,-k)
    
    else:
        x = quary[1]
        print(sum_tree(tree,x))
        