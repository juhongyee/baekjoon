import sys
import bisect

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

prefix_A = []
for i in range(n):
    sumation = 0
    for j in range(i,n):
        sumation += A[j]
        prefix_A.append(sumation)

prefix_B = []
for i in range(m):
    sumation = 0
    for j in range(i,m):
        sumation += B[j]
        prefix_B.append(sumation)

prefix_A.sort()
prefix_B.sort()

#answer
ans = 0

for i in range(len(prefix_A)):
    val = T - prefix_A[i]
    
    ans += bisect.bisect_right(prefix_B,val)-bisect.bisect_left(prefix_B,val)

print(ans)