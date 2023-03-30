N,M = 0,0
arr = [0 for i in range(10)]

def back_tracking(cur,length):
    if(length == M):
        for i in range(0,M):
            if(i!=M-1):
                print(arr[i],end=' ')
            else:
                print(arr[i])
        return
    
    else:
        for i in range(cur,N+1):
            arr[length] = i
            back_tracking(i+1,length+1)

N,M = map(int,input().split())
back_tracking(1,0)