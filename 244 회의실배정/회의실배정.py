import sys
from collections import deque

N = int(input())

conference = []

for i in range(N):
    conference.append(tuple(map(int,sys.stdin.readline().split())))

conference.sort(key=lambda x : (x[1],x[0]))

ans = []

ans.append(conference[0])

for i in range(1,len(conference)):
    if(ans[len(ans)-1][1]<=conference[i][0]):
        ans.append(conference[i])

print(len(ans))