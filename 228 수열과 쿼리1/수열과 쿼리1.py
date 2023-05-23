import sys
import bisect

class Segment_tree:
    def __init__(self,arr):
        self.arr = arr
        self.tree = [0]*(4*len(self.arr))
        self.build_tree(0,len(self.arr)-1,0)
        
    def build_tree(self,start,end,node):
        if(start==end):
            self.tree[node] = [self.arr[start]]
            return self.tree[node]

        mid = (start+end)//2
        left = self.build_tree(start,mid,2*node+1)
        right = self.build_tree(mid+1,end,2*node+2)
        
        arr = []
        idx_l = 0
        idx_r = 0
        
        while(idx_l != len(left) and idx_r != len(right)):
            if(left[idx_l]<right[idx_r]):
                arr.append(left[idx_l])
                idx_l += 1
            else:
                arr.append(right[idx_r])
                idx_r += 1
        
        while(idx_l != len(left)):
            arr.append(left[idx_l])
            idx_l += 1
        
        while(idx_r != len(right)):
            arr.append(right[idx_r])
            idx_r += 1
        
        self.tree[node] = arr
        
        return self.tree[node]
    
    def Query(self,start,end,node,left,right,val):
        if(start>right or end<left):
            return 0
        if(left<=start and end<=right):
            arr = self.tree[node]
            idx = bisect.bisect_right(arr,val)

            return len(arr)-idx

        mid = (start+end)//2
        left_val = self.Query(start,mid,2*node+1,left,right,val)
        right_val = self.Query(mid+1,end,2*node+2,left,right,val)
        
        return left_val+right_val
        
N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
seg_tree = Segment_tree(arr)

M = int(sys.stdin.readline())

for _ in range(M):
    i,j,k = map(int,sys.stdin.readline().split())
    print(seg_tree.Query(0,len(seg_tree.arr)-1,0,i-1,j-1,k))