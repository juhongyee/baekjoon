from collections import deque
import math
N = int(input())

arr = list(map(int,input().split()))

min_arr = [0 for i in range(20*100000)]

for i in range(2**N):
    
    temp = deque()
    
    for j in range(N):
        if((i&(1<<j))!=0):
            temp.append(arr[j])
    min_arr[sum(temp)] = 1

for i in range(1,20*100000):
    if(min_arr[i] == 0):
        print(i)
        break