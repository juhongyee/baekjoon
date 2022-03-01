import sys

def makeS(arr,N):
    #행 더하기
    for i in range(1,N+1):
        for j in range(1,N):
            arr[i][j+1] += arr[i][j]

    #열 더하기
    for i in range(1,N+1):
        for j in range(1,N):
            arr[j+1][i] += arr[j][i]

def query(arr,x1,y1,x2,y2):
    return arr[x2][y2]-(arr[x1-1][y2]+arr[x2][y1-1])+arr[x1-1][y1-1]

#크기 N, 합을 구해야 하는 횟수 M
N,M = map(int,input().split())

arr = [[0 for i in range(N+1)] for j in range(N+1)] 

for i in range(N):
    arr[i+1] = [0]+list(map(int,sys.stdin.readline().split()))
#print(arr)
makeS(arr,N)
#print(arr)
for i in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(query(arr,x1,y1,x2,y2))

    
    
    
