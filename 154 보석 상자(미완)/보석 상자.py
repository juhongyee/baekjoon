import sys

#아이들의 수, 색상의 수
N,M = map(int,input().split())

juwerly = [0 for i in range(M)]

sum = 0
max = 0
for i in range(M):
    juwerly[i] = int(sys.stdin.readline())
    sum += juwerly[i]
    if(max<juwerly[i]):
        max = juwerly[i]

average = sum//N

for i in range()

print(average+1)



