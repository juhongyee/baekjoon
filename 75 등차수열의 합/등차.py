import math
def extended_gcd(a,b):
    if a == 0:
        return [b,0,1]

    else :
        c= extended_gcd(b%a,a)
        gcd, x, y = c[0], c[1], c[2]
        return [gcd, y-(b//a)*x,x]

left = int(input())
right = int(input())
k = int(input())
count = 0
for i in range(left,right+1):
    if((2*i)%k == 0):
        c = extended_gcd(2,k-1)
        if(((2*i)//k)%c[0] ==0):
            a = c[1]*((2*i//k)/c[0])
            b = c[2]*((2*i//k)/c[0])
            a_cal = max(-1*a/(k-1),-1*b/(-2))
            b_cal = min(-1*a/(k-1),-1*b/(-2))

            if(a_cal>math.floor(b_cal)+1):
                count += 1

print(count)

'''if(i==4):
                print(a,b,a_cal,b_cal)'''
'''print(extended_gcd(2,4))
            
if(i==4):
    print(a,b,a_cal,b_cal)'''
