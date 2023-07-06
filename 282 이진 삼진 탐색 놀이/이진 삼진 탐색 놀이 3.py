import sys
import math
Q = int(input())

def b_search(left,right,count):
    if(left>right):
        return count-1
    mid = (left+right)//2
    return b_search(mid+1,right,count+1)

def t_search(left,right,count,flag):
    if left>right:
        return count-flag
    diff = (right-left)//3
    left_t = left+diff
    right_t = right-diff
    
    if(left_t==right_t):
        return max(t_search(right_t+1,right,count+1,1),t_search(left_t+1,right_t-1,count+1,1))
    else:
        return t_search(right_t+1,right,count+2,2)

for i in range(Q):
    N = int(sys.stdin.readline())
    print(b_search(0,N-1,0),end= ' ')
    print(t_search(0,N-1,0,0))