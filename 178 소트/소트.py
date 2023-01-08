import sys
from collections import deque

input_list = [0 for i in range(1001)]

N = int(input())

num_list = list(map(int,sys.stdin.readline().split()))

for i in range(N):
    input_list[num_list[i]] += 1

sorted = deque()

maximum = 0
for i in range(1001):
    if(input_list[i] != 0):
        maximum = i

#앞서 반복문 돌기
for i in range(0,maximum+1):
    if(input_list[i] != 0): #만약 0이 아니라면 greedy choice
        for j in range(input_list[i]):
            sorted.append(i)
        
        input_list[i] = 0
        
        if(i<maximum-1):
            #근데 다음 숫자도 0이 아니다?
            if(input_list[i+1] != 0): #오버플로우 방지 아직 부족
                
                #그 다음부터 list iteration
                for j in range(i+2,maximum+1):
                    #나오자마자 pick
                    if(input_list[j]!=0):
                        sorted.append(j)
                        input_list[j] -= 1
                        break
                        
        elif(i==maximum-1 and input_list[maximum]!=0):#i가 maximum-1일 때도 있고 maximum일 때도 있는 경우
            #999 다시 빼내기
            count = 0
            while(sorted[-1]==maximum-1):
                sorted.pop()
                count+=1
                if(not sorted):
                    break
            #1000 넣기
            for j in range(input_list[maximum]):
                sorted.append(maximum)
            for j in range(count):
                sorted.append(maximum-1)
            

for i in range(N):
    print(sorted[i],end ='')
    if(i!=N-1):
        print(' ',end='')
        