from collections import deque
import sys

given = deque(map(deque,sys.stdin.readline().split()))

ans = []

token = ['<','>','&','|','(',')']

while(given):
    A = given.popleft()
    string = []
    while(A):
        B = A.popleft()
        if(B in token):
            if(len(string)>0):
                ans.append(string)
                string = []
            
            if(B == '&' or B == '|'):
                A.popleft()
                ans.append(B+B)
            else:
                ans.append(B)
        
        else:
            string.append(B)
    if(len(string)>0):
        ans.append(string)

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end='')
    print(' ',end='')
