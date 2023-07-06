import sys
import bisect

N,M = map(int,sys.stdin.readline().split())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for _ in range(M):
    val = int(sys.stdin.readline())
    loc = bisect.bisect_left(arr,val)
    
    if(loc>=len(arr) or arr[loc] != val):
        print(-1)
    else:
        print(loc)