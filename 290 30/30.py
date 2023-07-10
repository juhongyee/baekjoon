import sys
arr = sys.stdin.readline().strip()

arr_num = []

for i in range(len(arr)):
    arr_num.append(int(arr[i]))

arr_num.sort(reverse=True)

if(sum(arr_num)%3 != 0 or arr_num[-1] !=0):
    print(-1)
else:
    for i in range(len(arr_num)):
        print(arr_num[i],end='')