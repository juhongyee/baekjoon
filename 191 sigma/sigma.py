import sys
import math
mod = 1000000007

M = int(input())
arr = []
for i in range(M):
    arr.append(list(map(int,sys.stdin.readline().split())))

def mod_Inv(b,n):
    if(n==1):
        return b%mod
    
    else:
        if(n%2==0):
            return (mod_Inv(b,n//2)**2)%mod
        else:
            return ((mod_Inv(b,n//2)**2)*b)%mod


b = 1
for i in range(M):
    b *= arr[i][0]
    b %= mod

sum = 0
for i in range(M):
    a_i = arr[i][1]
    b_i = arr[i][0]
    gcd = math.gcd(a_i,b_i)
    
    a_i //= gcd
    b_i //= gcd
    sum += (a_i*b*(mod_Inv(b_i,mod-2)))%mod
    sum %= mod

print((sum*mod_Inv(b,mod-2))%mod)
