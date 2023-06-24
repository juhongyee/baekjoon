import sys
import heapq

N = int(input())

ans = 0
arr_plus = []
arr_minus = []
for _ in range(N):
    val = int(sys.stdin.readline())
    if(val>0):
        arr_plus.append(-val)
    else:
        arr_minus.append(val)

heapq.heapify(arr_plus)
heapq.heapify(arr_minus)
    
while arr_plus:
    A = heapq.heappop(arr_plus)
    if(A==-1):
        ans += len(arr_plus)+1
        break
    if not arr_plus:
        ans -= A
        break
    
    B = heapq.heappop(arr_plus)
    if(B==-1):
        ans += len(arr_plus)-A+1
        break
    
    ans += A*B

while arr_minus:
    A = heapq.heappop(arr_minus)
    if(A==0):
        break
    
    if not arr_minus:
        ans += A
        break
    
    B = heapq.heappop(arr_minus)
    
    ans += A*B
    
    
print(ans)