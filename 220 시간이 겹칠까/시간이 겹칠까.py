import sys

N = int(sys.stdin.readline())

sumation = [0]*1000002
for i in range(N):
    start,end = map(int,sys.stdin.readline().split())
    sumation[start] += 1
    sumation[end+1] += -1

now = 0
for i in range(1,1000001):
    now += sumation[i]
    sumation[i] = now

Q = int(sys.stdin.readline())

Quary = list(map(int,sys.stdin.readline().split()))

for i in range(Q):
    print(sumation[Quary[i]])