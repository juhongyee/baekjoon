import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()
height = []
ans = -1
for i in range(N):
    cur = int(sys.stdin.readline())
    height.append(cur)
    
    while stack and height[stack[-1]]>cur:
        h = height[stack.pop()]
        w = i if not stack else i-stack[-1]-1
        ans = max(ans,h*w)
    stack.append(i)
    
while(stack):
    idx = stack.pop()
    h = height[idx]
    w = len(height) if not stack else len(height)-idx
    ans = max(ans,h*w)

print(ans)

