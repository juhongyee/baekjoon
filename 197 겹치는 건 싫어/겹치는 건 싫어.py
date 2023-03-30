from collections import deque
import sys


N,K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
deck = [0 for i in range(100001)]

maximum = 1
cnt = 0
last_index = len(arr)-1

for i in range(len(arr)-1,-1,-1):
    if(deck[arr[i]] == 0):
        deck[arr[i]] = deque()
        
    if(len(deck[arr[i]])==K):
        index = deck[arr[i]].pop()
        deck[arr[i]].appendleft(i)
        if(last_index < index):
            cnt += 1
        else:
            last_index = index
            cnt =index-i
    else:
        deck[arr[i]].appendleft(i)
        cnt += 1
    if(cnt>maximum):
        maximum = cnt

print(maximum)
