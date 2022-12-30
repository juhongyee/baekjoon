from collections import deque
N,S = map(int,input().split())

arr = list(map(int,input().split()))

count = 0
for i in range(2**N):
    
    temp = deque()
    
    for j in range(N):
        if((i&(1<<j))!=0):
            temp.append(arr[j])
    
    if(sum(temp) == S and temp):
        count += 1

print(count)
    