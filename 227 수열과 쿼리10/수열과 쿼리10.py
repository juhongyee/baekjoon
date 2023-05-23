import sys

class segment_tree:
    
    def __init__(self,arr):
        self.arr = arr
        self.tree = [0]*(4*len(arr))
        self.build_tree(0,len(arr)-1,0)
        
    def build_tree(self,start,end,node):
        if(start==end):
            self.tree[node] = [self.arr[start],0]
            return self.tree[node]
        
        mid = (start+end)//2
        
        left = self.build_tree(start,mid,2*node+1)
        right = self.build_tree(mid+1,end,2*node+2)

        idx_l = 0
        idx_r = 0
        
        maximum = [-1,-1]
        
        for i in range(2):
            if(left[idx_l]>=right[idx_r]):
                maximum[i] = left[idx_l]
                idx_l += 1
            else:
                maximum[i] = right[idx_r]
                idx_r += 1
        
        self.tree[node] = maximum
        
        return maximum
    
    #하기 전에 arr 내용 바꿔야 함
    def update(self,start,end,node,idx):
        if(start==end):
            self.tree[node][0] = self.arr[idx]
            return
        
        mid = (start+end)//2
        if(start<=idx<=mid):
            self.update(start,mid,2*node+1,idx)
        else:
            self.update(mid+1,end,2*node+2,idx)
        
        left = self.tree[2*node+1]
        right = self.tree[2*node+2]
        
        idx_l = 0
        idx_r = 0
        
        maximum = [-1,-1]
        
        for i in range(2):
            if(left[idx_l]>=right[idx_r]):
                maximum[i] = left[idx_l]
                idx_l += 1
            else:
                maximum[i] = right[idx_r]
                idx_r += 1
        
        self.tree[node] = maximum
    
    def Query(self,start,end,node,left,right):
        if(start>right or end<left):
            return [0,0]
        
        if(left<=start and end<=right):
            return self.tree[node]
        
        mid = (start+end)//2
        left_val = self.Query(start,mid,2*node+1,left,right)
        right_val = self.Query(mid+1,end,2*node+2,left,right)
        
        idx_l = 0
        idx_r = 0
        
        maximum = [-1,-1]
        
        for i in range(2):
            if(left_val[idx_l]>=right_val[idx_r]):
                maximum[i] = left_val[idx_l]
                idx_l += 1
            else:
                maximum[i] = right_val[idx_r]
                idx_r += 1
        
        return maximum
        
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

seg_tree = segment_tree(arr)
#print(seg_tree.tree)
M = int(sys.stdin.readline())

for _ in range(M):
    num,l,r = map(int,sys.stdin.readline().split())
    
    if(num==1):
        seg_tree.arr[l-1] = r
        seg_tree.update(0,len(arr)-1,0,l-1)
    
    if(num==2):
        print(sum(seg_tree.Query(0,len(arr)-1,0,l-1,r-1)))