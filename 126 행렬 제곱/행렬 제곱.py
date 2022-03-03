def fpow(A,b):
    if(b==1):
        return A

    else:
        x = fpow(A,b//2)
        if(b%2==0):
            return m_product(x,x)
        else:
            return m_product(m_product(x,x),A)

def m_product(A,B):
    C = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(0,N):
                C[i][j] += (A[i][k]*B[k][j])
                C[i][j] %= 1000

    return C
    

#행렬의 크기 N, B제곱
global N
N,B = map(int,input().split())

A = [[0 for i in range(N)] for j in range(N)]

#행렬 입력
for i in range(N):
    A[i] = list(map(int,input().split()))

k = fpow(A,B)

for i in range(N):
    for j in range(N):
        print(k[i][j]%1000,end=' ')
    print('')
