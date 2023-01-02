def check(x,y,X,N):
    #x check, X의 i번째 값에는 x가 i일 때 좌표 저장, 고로 (-1,-1)이면 없음.
    if(X[x]!=(-1,-1)):
        return False
    
    #diagonal check
    for coordinate in X:
        if(coordinate!=(-1,-1)):
            cal_x = abs(x-coordinate[0])
            cal_y = abs(y-coordinate[1])
            
            if(cal_x==cal_y):
                return False
    
    return True

def queen(idx,X,N,count):
    #idx == y좌표, iterate하는 i는 x좌표
    if(idx==N-1):
        for i in range(N):
            if(check(i,idx,X,N)):
                count[0] += 1
    
    else:
        for i in range(N):
            if(check(i,idx,X,N)):
                X[i] = (i,idx)
                queen(idx+1,X,N,count)
                X[i] = (-1,-1)
        
N = int(input())

X = [(-1,-1) for i in range(N)]

count = [0]

queen(0,X,N,count)

if(N==1):
    print(1)
else: 
    print(count[0])