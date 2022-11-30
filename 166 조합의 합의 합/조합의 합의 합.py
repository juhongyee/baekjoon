import math

mod = 10**9+7

def pow(n,p):
    if(p == 2):
        return (n**2)%mod
    if p%2==0:
        return pow((n**2)%mod,p//2)
    else:
        return(((n*pow(n,p-1))%mod))


sum_of_combination = 0

M = int(input())

#2C1로 cal 초기화
cal = 6

for n in range(3,M+1):
    cal = (cal*(2*n-1))%mod
    cal = (cal*(2*n))%mod
    cal = (cal*pow(n*n,mod-2))%mod
    sum_of_combination += cal

print(sum_of_combination%mod)