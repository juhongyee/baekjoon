import sys
from collections import deque
N = int(input())

stack = deque()
count = 0

for _ in range(N):
    height = [int(sys.stdin.readline()),1]
    
    if(not stack):
        stack.append(height)
    
    else:
        while(stack[-1][0]<height[0]):
            item = stack.pop()
            count += item[1]
            if(not stack):
                break
        
        if(not stack):
            stack.append(height)
        else:
            if(stack[-1][0] == height[0]):
                stack[-1][1] += 1
            else:
                stack.append(height)
        
        if(len(stack) != 1):
            count += stack[-1][1]
        else:
            count += (stack[-1][1]-1)
            
print(count)