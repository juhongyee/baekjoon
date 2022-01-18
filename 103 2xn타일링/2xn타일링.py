n = int(input())
#n번째 타일링을 구할것

A = list(range(n+1))
#n까지의 list

#1,2인 경우
A[1] = 1
if(n>=2):
    A[2] = 2

if(n<=2):
    print(A[n])
else:
    #새로운 타일이 들어갈 때 2가지 경우만 있을 수 있음.
    for i in range(3,n+1):
        A[i] = A[i-1]+A[i-2]

    print(A[n]%10007)
