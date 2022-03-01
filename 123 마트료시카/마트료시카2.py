import sys

#인형의 개수
N = int(input())
max_num = 10**5+1
doll = list(map(int,sys.stdin.readline().split()))
num_list = [0 for i in range(max_num+1)]

start = 1
revenue_sum = 0

for i in range(0,N):
    num_list[doll[i]] += 1

while(start != max_num):
    length = [0,start]
    if(num_list[start] >= 1):
        for i in range(start,max_num+1):
            if(num_list[i] != 0):
                length[0] += 1
                length[1] = i
                num_list[i] -= 1
            else:
                revenue_sum += length[0]*length[1]
                break
    else:
        start += 1
            
print(revenue_sum)
