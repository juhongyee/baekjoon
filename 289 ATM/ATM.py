import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

prefix = 0
ans = 0
for i in range(N):
    ans += (prefix+arr[i])
    prefix += arr[i]

print(ans)