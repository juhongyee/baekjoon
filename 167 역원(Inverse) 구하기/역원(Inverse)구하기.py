
def extended_gcd(a,b):
    if a== 0:
        return [b,0,1]
    else:
        c = extended_gcd(b%a,a)
        gcd, x, y = c[0], c[1], c[2]
        return [gcd,y-(b//a)*x,x]
    
N,A = map(int,input().split())

additive_inverse = 0
productive_inverse = 0

additive_inverse = N-A

#Ax = 1(mod N) -> Ax-Ny = 0
c = extended_gcd(A,N)

if(c[0]!=1):
    productive_inverse = -1

else:
    productive_inverse = c[1]%N

print(additive_inverse,productive_inverse)