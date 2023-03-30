from collections import deque #스택을 사용해서 풀 예정
import sys

string = list(sys.stdin.readline().rstrip())
target = sys.stdin.readline().rstrip()

cnt_target = 0 #현재 체크해야할 target의 index 다음에 얘가 나와야 함.
mem_tar = deque()
stack = deque()

#시간복잡도 O(n)을 위해 하나씩 돌 예정
for i in range(len(string)):
    cnt = string[i]
    #도달하면 다 pop해서 -1로 만듦.
    if(cnt_target == len(target)):
        for j in range(len(target)):
            string[stack.pop()] = -1
        if(mem_tar):
            cnt_target = mem_tar.pop()
        else:
            cnt_target = 0

    if(cnt == target[0]):#다시 시작
        stack.append(i)
        mem_tar.append(cnt_target)
        cnt_target = 1
        
    #다음 차례에 올 녀석이 맞다면 넣고
    elif(cnt == target[cnt_target]):
        stack.append(i)
        cnt_target += 1
    
    #다음차례가 아니라면 mem_tar에서 계속 꺼내보고 없으면 stack초기화(X 이런경우는 없었다.), 걍 초기화
    else:
        mem = deque()
        stack = deque()
        cnt_target = 0

if(cnt_target == len(target)):
        for j in range(len(target)):
            string[stack.pop()] = -1

flag = True
for i in range(len(string)):
    if(string[i] != -1):
        flag = False
        print(string[i],end = '')

if(flag):
    print("FRULA")