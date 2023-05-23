import sys

N,H = map(int,sys.stdin.readline().split())

mem_d = [0]*(H+2)
mem_A = [0]*(H+2)

for i in range(1,N+1):
    if(i%2==1):
        end = int(sys.stdin.readline())
        mem_d[1] += 1
        mem_d[end+1] -= 1
    
    else:
        mem_A[H] += 1
        end = int(sys.stdin.readline())
        mem_A[H-end] -= 1

now = 0
for i in range(1,H+1):
    now += mem_d[i]
    mem_d[i] = now
    
now = 0
for i in range(H,-1,-1):
    now += mem_A[i]
    mem_A[i] = now

for i in range(1,H+1):
    mem_d[i] += mem_A[i]

minimum = float('inf')
for i in range(1,H+1):
    if(minimum>mem_d[i]):
        minimum = mem_d[i]

count = 0
for i in range(1,H+1):
    if(minimum == mem_d[i]):
        count += 1

print(minimum,count)