import sys
from collections import deque

def dist(A,B):
    
    return (abs(A[0]-B[0]))**2+(abs(A[1]-B[1]))**2

def nearest_points(arr,low,high):
    if(high<=low):
        return 0
    elif(high-low==1):
        return dist(arr[high],arr[low])
    mid = (high+low)//2
    val1 = nearest_points(arr,low,mid) #왼쪽이 항상 하나 더 많음
    val2 = nearest_points(arr,mid+1,high)
    
    if(val1<=val2):
        return val1
    else:
        return val2
    
    

N = int(input())

arr = deque()

for i in range(N):
    point = tuple(map(int,sys.stdin.readline().split()))
    arr.append(point)

print(nearest_points(arr,0,N-1))