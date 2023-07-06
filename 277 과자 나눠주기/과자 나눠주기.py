import sys

M,N = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
left = 1
right = arr[N-1]

while left<=right:
    mid = (left+right)//2
    count = 0

    for val in arr:
        count += (val//mid)
    
    if(count>=M):
        left = mid+1
    else:
        right = mid-1

print(right)