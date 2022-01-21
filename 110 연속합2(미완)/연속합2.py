import sys
#n으로 끝내는 법 강구
def find_max(A,n):
    max = A[0]
    max2 = -100000001
    temp = 0
    for i in range(0,n):
        if(temp + A[i]<0):
            if(i!=n-1):
                max2 = find_max2(A[i+1:n],n-i-1)
                if(temp+max2>max):
                    max = temp + max2
            temp = 0
            if(temp+A[i]>max):
                max = temp+A[i]
            continue
        else:
            if(max<temp+A[i]):
                max = temp+A[i]
            temp += A[i]

    return max

def find_max2(A,n):
    max = A[0]
    temp = 0
    for i in range(0,n):
        if(temp + A[i]<0):
            temp = 0
            if(temp+A[i]>max):
                max = temp+A[i]
            continue
        else:
            if(max<temp+A[i]):
                max = temp+A[i]
            temp += A[i]

    return max

#수 개수 입력
n = int(input())

#수 저장 리스트
A = list(map(int,sys.stdin.readline().split()))

max = find_max(A,n)

print(max)
