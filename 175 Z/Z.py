def Z_recur(N,r,c,current,start_x,start_y):
    if(N==0):
        return current
    else:
        if(r<start_x+(2**(N-1))):
            if(c<start_y+(2**(N-1))):
                #제 2사분면일 때는 이동X
                return Z_recur(N-1,r,c,current,start_x,start_y)
            else:
                #제 1사분면
                current += 1*((2**(N-1))**2)
                return Z_recur(N-1,r,c,current,start_x,start_y+(2**(N-1)))
            
        else:
            if(c<start_y+(2**(N-1))):
                #제3사분면
                current += 2*((2**(N-1))**2)
                return Z_recur(N-1,r,c,current,start_x+(2**(N-1)),start_y)
            else:
                #제 4사분면
                current += 3*((2**(N-1))**2)
                return Z_recur(N-1,r,c,current,start_x+(2**(N-1)),start_y+(2**(N-1)))
            
N,r,c = map(int,input().split())
print(Z_recur(N,r,c,0,0,0))
