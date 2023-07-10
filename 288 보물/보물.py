import sys
N = int(sys.stdin.readline())

arr1 = list(map(int,sys.stdin.readline().split()))
arr2 = list(map(int,sys.stdin.readline().split()))

arr1.sort()
arr2.sort(reverse=True)

ans = 0
for i in range(N):
    ans += arr1[i]*arr2[i]
print(ans)