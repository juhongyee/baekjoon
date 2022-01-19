import heapq
import sys

#로그의 줄 수,플레이어 수
T,N = map(int,input().split())

position = [1 for i in range(N+1)]
item_list = [[0 for j in range(54)] for i in range(N+1)]
cheating_list = []
blocking_list = []

block_check = [0 for i in range(N+1)]
num_cheat = 0
num_block = 0

#T번 log를 받을 것
for i in range(1,T+1):
    #log입력 및 형 변환
    log = sys.stdin.readline().split()
    num = int(log[0])
    player = int(log[1])
    action = log[2]
    objection = int(log[3])
    #Craftmode일 때는 두 개 받아야 함.
    if(action == 'C'):
        objection2 = int(log[4])

    if(action == 'M'):
        #이동
        position[player] = objection
    elif(action == 'F'):
        #farming
        if(objection != position[player]):
            #cheating1.
            num_cheat += 1
            heapq.heappush(cheating_list,num)
        item_list[player][objection] += 1
    elif(action == 'C'):
        #Crafting
        a= not(item_list[player][objection])
        b= not(item_list[player][objection2])
        if(a or b):
            #cheating2.
           num_cheat += 1
           heapq.heappush(cheating_list,num)
        if(not a):
             item_list[player][objection] -= 1
        if(not b):
             item_list[player][objection2] -= 1
    else:
        #Attack
        if(position[player] != position[objection]):
            #위치 다름 cheating3.
            if(not block_check[player]):
                num_block += 1
                heapq.heappush(blocking_list,player)
            block_check[player] = 1
            num_cheat += 1
            heapq.heappush(cheating_list,num)
            
#결과 출력
print(num_cheat)
if(num_cheat):
    for i in range(0,num_cheat):
        print(heapq.heappop(cheating_list),end = ' ')
    print('')
print(num_block)

#blocking_list_make
if(num_block):
    for i in range(0,num_block):
        print(heapq.heappop(blocking_list),end = ' ')
