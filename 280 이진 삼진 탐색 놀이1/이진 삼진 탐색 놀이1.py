N = int(input())

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

arr_b = [0]*N
arr_t = [0]*N
b_search(arr_b,0,N-1,0)
t_search(arr_t,0,N-1,0)

ans_1 = 0
ans_2 = 0
ans_3 = 0
for i in range(N):
    if(arr_b[i]<arr_t[i]):
        ans_1 += 1
    elif(arr_b[i]==arr_t[i]):
        ans_2 += 1
    else:
        ans_3 += 1

print(ans_1)
print(ans_2)
print(ans_3)

print(arr_b)
print(arr_t)