from collections import deque

N,K = map(int,input().split())

queue_1 = deque()
queue_2 = deque()

answer = []
for i in range(1,N+1):
    queue_1.append(i)

count = 0
turn = queue_1
turn_n = queue_2
while(queue_1 or queue_2):
    while(turn):
        if(count==K-1):
            answer.append(turn.popleft())
            count = 0
        else:
            turn_n.append(turn.popleft())
            count+=1
    
    turn = queue_2 if turn is queue_1 else queue_1

print('<',end='')

for i in range(len(answer)):
    print(answer[i],end='')
    if(i!=len(answer)-1):
        print(',',end = ' ')

print('>')