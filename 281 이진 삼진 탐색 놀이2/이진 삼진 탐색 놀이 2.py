import sys

Q = int(input())

def b_search(arr,left,right,count):
    if(left>right):
        return
    mid = (left+right)//2
    arr[mid] = count
    b_search(arr,left,mid-1,count+1)
    b_search(arr,mid+1,right,count+1)

def t_search(arr,left,right,count):
    if(left>right):
        return
    diff = (right-left)//3
    left_t = left+diff
    right_t = right-diff
    
    if(left_t==right_t):
        arr[left_t] = count
    else:
        arr[left_t] = count
        arr[right_t] = count+1
    
    t_search(arr,left,left_t-1,count+2)
    t_search(arr,left_t+1,right_t-1,count+2)
    t_search(arr,right_t+1,right,count+2)

prefix_b = [[]]+[[0 for i in range(j)] for j in range(1,5001)]
prefix_t = [[]]+[[0 for i in range(j)] for j in range(1,5001)]
#fill the prefix
for i in range(1,5001):
    arr_b = [0]*i    
    arr_t = [0]*i
    b_search(arr_b,0,i-1,0)
    t_search(arr_t,0,i-1,0)
    
    sum_b = 0
    sum_t = 0
    for j in range(i):
        sum_b += arr_b[j]
        sum_t += arr_t[j]
        
        prefix_b[i][j] = sum_b
        prefix_t[i][j] = sum_t

for i in range(Q):
    N,S,E = map(int,sys.stdin.readline().split())
    if(S==0):
        print(prefix_t[N][E]-prefix_b[N][E])
    else:
        print((prefix_t[N][E]-prefix_t[N][S-1])-(prefix_b[N][E]-prefix_b[N][S-1]))