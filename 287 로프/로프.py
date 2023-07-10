import sys

N = int(sys.stdin.readline())

rope = []

for i in range(N):
    rope.append(int(sys.stdin.readline()))
    
rope.sort()

maximum = 0

for i in range(N):
    maximum = max(maximum,(N-i)*rope[i])

print(maximum)