import sys
import math
class SegmentTree:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.tree = [0]*(4*len(arr))
        self.build_tree(0,len(arr)-1,0)
    
    def build_tree(self,start,end,node):
        if start==end: #leaf node
            self.tree[node] = self.arr[start]
        
        else:
            mid = (start+end)//2
            self.build_tree(start,mid,2*node+1)#0번부터면 2n+1과 2n+2
            self.build_tree(mid+1,end,2*node+2)
            self.tree[node] = min(self.tree[2*node+1],self.tree[node*2+2])
    
    def update(self,start,end,node,index,value):
        if start==end:
            self.arr[index] = value
            self.tree[node] = value
        
        else:
            mid = (start+end)//2
            if index>=start and index<=mid:
                self.update(start,mid,2*node+1,index,value)
            else:
                self.update(mid+1,end,2*node+2,index,value)
            self.tree[node] = min(self.tree[2*node+1],self.tree[2*node+2])

    def query(self,start,end,left,right,node):
        if(start>right or left>end):
            return math.inf
        elif start>=left and end <= right:
            return self.tree[node]
        else:
            mid = (start+end)//2
            left_min = self.query(start,mid,left,right,2*node+1)
            right_min = self.query(mid+1,end,left,right,2*node+2)
            
            return min(left_min,right_min)
            

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
M = int(input())

Tree = SegmentTree(arr)
for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    
    if(a==1):
        Tree.update(0,len(arr)-1,0,b-1,c)
    else:
        print(Tree.query(0,len(arr)-1,b-1,c-1,0))