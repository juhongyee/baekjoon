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

#앞에서부터 계산, 뒤부터 계산

front = [0 for i in range(n)]
back = [0 for i in range(n)]

LIS(A,n,front)
LIS(A[-1::-1],n,back)

max = front[0]+back[n-1]
for i in range(1,n-1):
    if(max<front[i]+back[n-1-i]):
        max = front[i]+back[n-1-i]
print(front)
print(back)
print(max-1)

