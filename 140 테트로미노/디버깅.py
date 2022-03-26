import sys

#세로크기 N 가로크기 M

def calculate(A,x1,y1,N,M,count,maximum,memo,pre):
    count += 1
    if(count < 4):
        if(count == 2):
            for i in range(0,4):
                for j in range(0,4):
                    if(0<=x1+x[i]<N and 0<=y1+y[i]<M and 0<=x1+x[j]<N and 0<=y1+y[j]<M):
                        if(not(x[pre] == -1*x[i] and y[pre] == -1*y[i]) and not(x[pre] == -1*x[j] and y[pre] == -1*y[j])):
                            if(i!=j):
                                maximum[0] = max(maximum[0],memo+A[x1+x[i]][y1+y[i]]+A[x1+x[j]][y1+y[j]])
        for i in range(0,4):
            if(0<=x1+x[i]<N and 0<=y1+y[i]<M):
                if(pre != 5):
                    if(x[pre] == -1*x[i] and y[pre] == -1*y[i]):
                        continue
                calculate(A,x1+x[i],y1+y[i],N,M,count,maximum,memo+A[x1+x[i]][y1+y[i]],i)

    elif(count == 4):
        if(maximum[0]<memo):
            maximum[0] = memo

            
x = [1,0,-1,0]
y = [0,-1,0,1]
maximum = [-1]
N,M = map(int,input().split())

A = [[0 for i in range(N)] for j in range(M)]

for i in range(N):
    A[i] = list(map(int,sys.stdin.readline().split()))

for i in range(N):
    for j in range(M):
        calculate(A,i,j,N,M,0,maximum,A[i][j],5)

print(maximum[0])
