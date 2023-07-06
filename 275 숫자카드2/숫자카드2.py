import bisect

import bisect
import sys

def b_search(arr,target):
    l = bisect.bisect_left(arr,target)
    r = bisect.bisect_right(arr,target)
    
    return r-l

N = int(input())
card = list(map(int,sys.stdin.readline().split()))
M = int(input())
quary = list(map(int,sys.stdin.readline().split()))

card.sort()
ans = [b_search(card,quary[i]) for i in range(M)]
print(*ans)