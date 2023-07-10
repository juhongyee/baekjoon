import sys
import math
Q = int(input())

max_t = 0

def b_search(left,right,count):
    if(left>right):
        return count-1
    mid = (left+right)//2
    return b_search(mid+1,right,count+1)

def t_search(left,right,count,target):
    diff = (right-left)//3
    left_t = left+diff
    right_t = right-diff
    
    if(left_t == target):
        return count
    elif right_t==target:
        return count+1
    
    elif(left_t==right_t):
        return t_search(right_t+1,right,count+1,target)
    else:
        return t_search(right_t+1,right,count+2,target)

for i in range(Q):
    N = int(sys.stdin.readline())
    print(b_search(0,N-1,0),end= ' ')
    print(t_search(0,N-1,0,N-1))