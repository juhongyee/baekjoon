import sys
import heapq
#전자기기 개수 N, 콘센트 개수 M
N,M = 0,0
count = 0
time_sum = 0

N,M = map(int,input().split())

time = list(map(int,sys.stdin.readline().split()))

time.sort(reverse = True)
#print(time)

#콘센트에 끼운다는 행위를 우선순위큐로 구현
priority_queue = []

#initialize
for i in range(M):
    if(count<N):
        heapq.heappush(priority_queue,time[count])
        count += 1
#print(priority_queue)
while(len(priority_queue) != 0):
    temp = heapq.heappop(priority_queue)
    #print(temp)
    time_sum += temp
    #print(time_sum)
    for i in range(len(priority_queue)):
        priority_queue[i] -= temp
    
    tempcount = 1 #heap에서 몇 개의 item을 pop했는지 저장
    
    if(len(priority_queue)!=0):
        while(not priority_queue[0]):
            tempcount += 1
            heapq.heappop(priority_queue)
            if(len(priority_queue)==0):
                break

    for i in range(tempcount):
        if(count<N):
            heapq.heappush(priority_queue,time[count])
            count +=1

print(time_sum)
