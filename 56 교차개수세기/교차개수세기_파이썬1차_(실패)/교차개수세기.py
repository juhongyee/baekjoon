import sys

def makeS(A,N):
    sum_list = [[0 for i in range(N+1)] for j in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(0,N):
            sum_list[i][j+1] = sum_list[i][j]+A[i][j+1]
    
    for i in range(1,N):
        for j in range(1,N+1):
            sum_list[i+1][j] += sum_list[i][j]

    return sum_list

def partial_sum(i,j,S,N):
    if(i==N and j==N):
        return 0
    
    elif(i!=N and j!=N):
        area1 = accum(S,1,j+1,i-1,N)
        area2 = accum(S,i+1,1,N,j-1)

        return area1+area2
    elif(i==N):
        return accum(S,1,j+1,i-1,N)

    elif(j==N):
        return accum(S,i+1,1,N,j-1)
    

def accum(S,x1,y1,x2,y2):
    return S[x2][y2] - (S[x1-1][y2]+S[x2][y1-1]) + S[x1-1][y1-1]

#N is the number of node, M is the number of edge
N,M = map(int,input().split())

#edges are remembered by 'A'
A = [[0 for i in range(N+1)] for j in range(N+1)]

#input edge
for k in range(M):
    i,j = map(int,sys.stdin.readline().split())
    A[i][j] = 1

#누적합 수열
S = makeS(A,N)

#calculate
cross = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if(A[i][j]==1):
            #print(i,j,partial_sum(i,j,S,N))
            cross += partial_sum(i,j,S,N)
print(cross//2)
