#maximum의 합을 구해서 minimum의 합을 빼자.

import sys
from collections import deque

def solve(N,arr):
    stack_max = deque()
    ans_max = arr[0]
    last_cal = arr[0]
    stack_max.append((arr[0],0))
    for i in range(1,N):
        val = (arr[i],i)
        
        if stack_max and stack_max[-1][0]>=val[0]:
            last_cal += val[0]
            stack_max.append(val)
            ans_max += last_cal
        else:
            if(stack_max and stack_max[-1][0]<val[0]):
                last_cal += val[0]
            
            before = stack_max[-1] #나 자신을 pop한거에서 빼는 거리로 시작
            
            while stack_max and stack_max[-1][0]<val[0]:
                now = stack_max.pop()
                last_cal += (val[0]-before[0])*(before[1]-now[1])
                before = now
            
            if(not stack_max):
                last_cal += (val[0]-before[0])*(now[1]+1)
            else:
                last_cal += (val[0]-before[0])*(before[1]-stack_max[-1][1])
                
            ans_max += last_cal
            stack_max.append(val)

    stack_min = deque()
    ans_min = arr[0]
    last_cal = arr[0]
    stack_min.append((arr[0],0))

    for i in range(1,N):
        val = (arr[i],i)
        
        if stack_min and stack_min[-1][0]<=val[0]:
            last_cal += val[0]
            stack_min.append(val)
            ans_min += last_cal
        else:
            if(stack_min and stack_min[-1][0]>val[0]):
                last_cal += val[0]
            
            before = stack_min[-1] #나 자신을 pop한거에서 빼는 거리로 시작
            
            while stack_min and stack_min[-1][0]>val[0]:
                now = stack_min.pop()
                last_cal += (val[0]-before[0])*(before[1]-now[1])
                before = now
            if(not stack_min):
                last_cal += (val[0]-before[0])*(now[1]+1)
            else:
                last_cal += (val[0]-before[0])*(before[1]-stack_min[-1][1])
            
            ans_min += last_cal
            stack_min.append(val)
    
    return ans_max,ans_min



N = int(input())
arr = list(map(int,sys.stdin.readline().split()))

ans_max,ans_min = solve(N,arr)
print(ans_max-ans_min)

#print(naive_approach(N,arr))

# def naive_approach(N,arr):
#     ans_max = 0
#     ans_min = 0
#     for i in range(N):
#         for j in range(i,N):
#             ans_max += max(arr[i:j+1])
#             ans_min += min(arr[i:j+1])
    
#     return ans_max,ans_min

#stub
# N = 4

# for x1 in range(1,10):
#     for x2 in range(1,10):
#         for x3 in range(1,10):
#             for x4 in range(1,10):
#                 arr = [x1,x2,x3,x4]
                
#                 ans_1,ans_2 = solve(N,arr)
#                 naive_1,naive_2 = naive_approach(N,arr)
                
#                 if(ans_1 != naive_1 or ans_2 != naive_2):
#                     print(ans_1)
#                     print(naive_1)
#                     print(ans_2)
#                     print(naive_2)
                    
#                     print(arr)

# print("Done!")
