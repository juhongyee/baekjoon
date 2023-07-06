import bisect
import sys

def b_search(arr,target):
    left = 0
    right = len(arr)-1
    
    # if(target==arr[left] or target == arr[right]):
    #     return 1
    
    while left<=right:
        mid = (left+right)//2
        if(arr[mid]==target):
            return 1
        elif(arr[mid]<target):
            left = mid+1
        else:
            right = mid-1
    
    return 0

N = int(input())
card = list(map(int,sys.stdin.readline().split()))
M = int(input())
quary = list(map(int,sys.stdin.readline().split()))

card.sort()
ans = [b_search(card,quary[i]) for i in range(M)]
print(*ans)

