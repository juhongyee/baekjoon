import sys
import math

def update(start,end,node,index,dif,tree):
    #print(node)
    if(index<start or end<index):
        return -1

    tree[node] = plus(tree[node],dif)

    if(start==end):
        return -1
    mid = (start+end)//2

    update(start,mid,node*2,index,dif,tree)
    update(mid+1,end,node*2+1,index,dif,tree)

def init(start,end,node,tree,OE):
    if(start==end):
        if(OE[start]%2==0):
            tree[node] = [0,1]
            return tree[node]
        else:
            tree[node] = [1,0]
            return tree[node]
    mid = (start+end)//2

    tree[node] = plus(init(start,mid,node*2,tree,OE),init(mid+1,end,node*2+1,tree,OE))

    return tree[node]

def plus(a,b):
    temp = [0,0]
    temp[0] = a[0]+b[0]
    temp[1] = a[1]+b[1]

    return temp

def odd_sum(start,end,node,left,right,tree):
    if(left>end or right<start):
        return 0
    if(left<=start and end<=right):
        return tree[node][0]

    mid = (start+end)//2

    return odd_sum(start,mid,node*2,left,right,tree)+odd_sum(mid+1,end,node*2+1,left,right,tree)

def even_sum(start,end,node,left,right,tree):
    #print(tree[node][1])
    #print(node)
    if(left>end or right<start):
        return 0
    if(left<=start and end<=right):
        return tree[node][1]

    mid = (start+end)//2

    return even_sum(start,mid,node*2,left,right,tree)+even_sum(mid+1,end,node*2+1,left,right,tree)

#수열의 크기
N = int(input())

#수열
sequence = [0]+list(map(int,sys.stdin.readline().split()))

#segment tree
tree_size = 2**(math.ceil(math.log(N)/math.log(2))+1)
tree = [[0,0] for i in range(tree_size)]

#쿼리의 개수
M = int(input())

init(1,N,1,tree,sequence)

for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    
    if(a==1):
        if(sequence[b]%2!=c%2):
            if(c%2==1):
                sequence[b] = c
                update(1,N,1,b,[1,-1],tree)
                #print(tree)
            else:
                sequence[b] = c
                update(1,N,1,b,[-1,1],tree)
                #print(tree)

    elif(a==2):
        print(even_sum(1,N,1,b,c,tree))

    else:
        print(odd_sum(1,N,1,b,c,tree))

                
