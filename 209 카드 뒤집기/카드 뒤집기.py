N = int(input())

arr = [0]*(N+1)
order = [0]*(N+1)
i = 1
j = N

print('YES')
if(N%2==0):
    first = 1
    last = N
    loc_1 = 0
    for i in range(N,1,-2):
        arr[first] = i
        first += 1
    for j in range(N-1,0,-2):
        arr[last] = j
        if(j==1):
            loc_1 = last
        last-=1
    
    for i in range(1,N+1):
        if(i!=N):
            print(arr[i],end = ' ')
        else:
            print(arr[i])
    
    now = loc_1
    while(now!=0 and now!=N+1):
        if(arr[now] != N):
            print(now,end = ' ')
        else:
            print(now)
        if(arr[now]%2==1):
            now -= arr[now]
        else:
            now += arr[now]

else:
    first = 1
    last = N
    loc_1 = 0
    for i in range(N,0,-2):
        arr[first] = i
        if(i==1):
            loc_1 = first
        first += 1
        
    for j in range(N-1,1,-2):
        arr[last] = j
        last-=1
    
    for i in range(1,N+1):
        if(i!=N):
            print(arr[i],end = ' ')
        else:
            print(arr[i])
    
    now = loc_1
    while(now!=0 and now!=N+1):
        if(arr[now]!=N):
            print(now,end = ' ')
        else:
            print(now)
        if(arr[now]%2==1):
            now += arr[now]
        else:
            now -= arr[now]