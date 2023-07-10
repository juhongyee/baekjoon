import sys
from collections import deque
arr = sys.stdin.readline().strip()

find = deque(['U','C','P','C'])

for i in range(len(arr)):
    if(arr[i] == find[0]):
        find.popleft()
    
    if(len(find) == 0):
        print("I love UCPC")
        exit()

print("I hate UCPC")