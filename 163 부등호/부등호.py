from collections import deque

global used
def recur(n,ineq,count,stack):
    if(count == len(ineq)):
        return 1
    
    sign = ineq[count]
    
    if(used[10] == 0):
        #range수정하면 큰 거 작은 거 바뀜
        if(sign == '>'):
            num_list = list(range(n,-1,-1))
        else:
            num_list = list(range(9,n-1,-1))
    else:
        if(sign == '>'):
            num_list = list(range(0,n))
        else:
            num_list = list(range(n+1,10))  
    
    empty_check = 0
    length = len(num_list)
    for i in range(length):
        if(used[num_list[i]]):
            num_list[i] = -1
            empty_check += 1
    
    if(empty_check==length):
        if(stack):
            stack.popleft()
        used[n] = 0
        return 0

    else:
        for i in num_list:
            if(i != -1):
                stack.appendleft(i)
                used[i] = 1
                if(recur(i,ineq,count+1,stack)):
                    return 1
        if(stack):
            stack.popleft()
        used[n] = 0
        return 0
            
#부등호 개수 입력
k = int(input())

#부등호 list 입력
ineq = list(input().split())

#used의 10번째는 maximum을 출력할지 minimum을 출력할지 결정
used = [0 for i in range(10)]
stack = deque()

for i in range(9,-1,-1):
    used = [0 for i in range(11)]
    used[i] = 1
    if(recur(i,ineq,0,stack)==1):
        print(i,end = '')
        while(stack):
            print(stack.pop(),end='')
        break
print()

for i in range(0,10):
    used = [0 for i in range(11)]
    used[i] = 1
    used[10] = 1
    if(recur(i,ineq,0,stack)==1):
        print(i,end = '')
        while(stack):
            print(stack.pop(),end='')
        break