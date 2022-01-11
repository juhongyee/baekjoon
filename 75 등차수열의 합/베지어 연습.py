def extended_gcd(a,b):
    if a == 0:
        return [b,0,1]

    else :
        c= extended_gcd(b%a,a)
        gcd, x, y = c[0], c[1], c[2]
        return [gcd, y-(b//a)*x,x]

def bezout(a,b):
    c= extended_gcd(a,b)

    return c

print(bezout(2,3))
