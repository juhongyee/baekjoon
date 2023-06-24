from collections import deque
import sys

def count_3(arr,N):
    mem = {0:0, N//2:0}
    for val in arr: #개수 세기
            mem[val%N] += 1
        
    for key in mem.keys():
        if(mem[key]>=2):#개수가 2 이상이면
            select = []
            rest = []
            for i in range(len(arr)): #모든 arr을 돌면서 어떤 걸 선택할지 정함
                if(arr[i]%N == key and len(select)<2):
                    select.append(arr[i])
                else:
                    rest.append(arr[i])
    
    return select,rest
                    
def solve(arr,N):
    if(N==2):
        ans,rest = count_3(arr,N)
        return ans,rest,sum(ans)

    now = deque(arr)
    
    mem_sumation = []
    mem_ans = []
    for i in range(3):
        for_recur = []
        for i in range(N-1):
            for_recur.append(now.popleft())
            
        ans,rest,sumation = solve(for_recur,N//2)
    
        mem_sumation.append(sumation)
        mem_ans.append(ans)
        
        for val in rest:
            now.appendleft(val)
    
    select,rest = count_3(mem_sumation,N)
    selected = select[0]%N
    select_count = 0
    ans = []
            
    for i in range(3):
        if(select_count<2 and mem_sumation[i]%N == selected):
            select_count += 1
            for j in range(len(mem_ans[i])):
                ans.append(mem_ans[i][j])
        else:
            for j in range(len(mem_ans[i])):
                now.appendleft(mem_ans[i][j])
    
    return ans,list(now),sum(ans)

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
ans = solve(arr,N)

print(*ans[0])

# N = 8
# for x1 in range():
#     for x2 in range(10):
#         for x3 in range(10):
#             for x4 in range(10):
#                 for x5 in range(10):
#                     for x6 in range(10):
#                         for x7 in range(10):
#                             arr = [x1,x2,x3,x4,x5,x6,x7]
#                             ans = solve(arr,N)
                            
#                             if sum(ans[0][0:N])%N != 0:
#                                 print(arr)
#                                 print(ans[0])
#                                 exit()

# print("done!")