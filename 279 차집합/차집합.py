import sys
import bisect

n_A,n_B = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A.sort()
B.sort()

ans = 0
ans_list = []
for i in range(n_A):
    idx = bisect.bisect_left(B,A[i])
    if(idx != n_B):
        if(A[i] == B[idx]):
            continue
    ans += 1
    ans_list.append(A[i])

print(ans)
print(*ans_list)