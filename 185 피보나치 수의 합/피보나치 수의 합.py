Prime = 1000000000
def product_mat(mat1,mat2):
    return [[((mat1[0][0]*mat2[0][0])%Prime+(mat1[0][1]*mat2[1][0])%Prime)%Prime,((mat1[0][0]*mat2[0][1])%Prime+(mat1[0][1]*mat2[1][1])%Prime)%Prime],[((mat1[1][0]*mat2[0][0])%Prime+(mat1[1][1]*mat2[1][0])%Prime)%Prime,((mat1[1][0]*mat2[0][1])%Prime+(mat1[1][1]*mat2[1][1])%Prime)%Prime]]

def pow_mat(n):
    if(n==1):
        return [[1,1],[1,0]]
    elif(n==0):
        return [[1,0],[0,1]]
    
    else:
        if(n%2==0):
            mat = pow_mat(n//2)
            return product_mat(mat,mat)
        else:
            mat = pow_mat(n//2)
            mat = product_mat(mat,mat)
            return product_mat(mat,[[1,1],[1,0]])

a,b = map(int,input().split())

if(a==1 and b==1):
    print(1)
else:
    print((pow_mat(b+1)[0][0]-pow_mat(a)[0][0])%Prime)