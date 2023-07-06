import sys
import math

T = int(sys.stdin.readline())

calcul_list = [0,1,1]

i = 3

def solve(n,k):
    ans = 0
    before = 1
    if k== 1:
        ans += calcul_list[1]*math.factorial(n-1)
    else:
        before = calcul_list[2]
        ans += calcul_list[2]*math.factorial(n-2)
        for i in range(3,k+1):
            ans += (k-(i-1))*before*(i-1)*math.factorial(n-i)
            before = (k-(i-1))*before*(i-1)
    
    return ans

for i in range(T):
    n,k = map(int,sys.stdin.readline().split())
    print(solve(n,k))
    