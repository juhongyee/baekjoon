import sys
N,K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

first = 1
second = 0
before = 0

for i in range(N-1):
    if(arr[i]<=K):
        first += 1
    else:
        second = max(second,first+before)
        before = first
        first = 1
second = max(second,first+before)
before = first
first = 1   
print(second)
