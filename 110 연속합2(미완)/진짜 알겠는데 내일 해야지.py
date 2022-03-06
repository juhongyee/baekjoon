import sys

#수 개수 입력
n = int(input())

#수 저장 리스트
A = list(map(int,sys.stdin.readline().split()))

max1 = A[0]
temp = 0
temp2 = 0
for i in range(0,n):
    if(temp + A[i]<0):
        temp2 = temp
        temp = 0
        if(temp+A[i]>max1 or max1<temp2+A[i]):
            max1 = max(temp+A[i],temp2+A[i])
        continue
    else:
        if(max1<temp+A[i] or max1<temp2+A[i]):
            max1 = max(temp+A[i],temp2+A[i])
        temp += A[i]
        temp2 += A[i]
print(max1)
