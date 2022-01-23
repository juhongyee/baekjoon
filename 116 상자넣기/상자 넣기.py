def LIS(A,n,memory):
    memory[0] = 1
    for i in range(1,n):
        max_length = 0
        for j in range(0,i):
            if(A[j]<A[i]):
                if(max_length<memory[j]):
                    max_length = memory[j]
        memory[i] = max_length+1

#수열의 크기
n = int(input())

#수열 저장
A = list(map(int,input().split()))

front = [0 for i in range(n)]
LIS(A,n,front)

max = -1

for i in range(0,n):
    if(front[i]>max):
        max = front[i]

print(max)
