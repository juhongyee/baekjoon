#recursive function
def recur(num,start,sum,arr):
    if(num == diff):
        if(num == 1):
            sum[0] += 1
            return 1
        
        #다음 recursive call,예를 들어 N=10,num=3이면, 16까지 돌 것
        for i in range(1,2*N-(num-1)):
            if(arr[i]==0 and arr[i+num-1+1]==0):
                #num이 0에 도달한 경우
                recur(num-1,i,sum,arr)
                arr[i] = 0
                arr[i+num-1+1] = 0
        
    else:
        arr[start] = num
        arr[start+num+1] = num
        
        if(num == 1):
            sum[0] += 1
            return 1

        #다음 recursive call,예를 들어 N=10,num=3이면, 16까지 돌 것
        if(diff == num-1):
            #diff가 num-1인 경우는 별로 안 중요함.
            recur(num-1,1,sum,arr)
        else:
            for i in range(1,2*N-(num-1)):
                if(arr[i]==0 and arr[i+num-1+1]==0 and diff != num-1):
                    #num이 0에 도달한 경우
                    recur(num-1,i,sum,arr)
                    arr[i] = 0
                    arr[i+num-1+1] = 0
            
                
                    
#랭퍼드 수열의 n,x,y입력
global N
N,X,Y = map(int,input().split())

global diff
diff = Y-X-1

sum = [0]

#랭퍼드 수열을 저장하는 array
arr = [0 for i in range(N*2+1)]

#수열의 X,Y번째를 diff로
arr[X] = diff
arr[Y] = diff

#Back_tracking with recursive call
if(N!=diff):
    for i in range(1,N):
        if(arr[i]==0 and arr[i+N+1]==0):
            recur(N,i,sum,arr)
            arr[i] = 0
            arr[i+N+1] = 0
else:
    for i in range(1,N+1):
        if(arr[i]==0 and arr[i+N-1+1]==0):
            recur(N-1,i,sum,arr)
            arr[i] = 0
            arr[i+N-1+1] = 0        

print(sum[0])