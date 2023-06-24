screen = [[' ' for i in range(3**7)] for j in range(3**7)]

def star(start,N):
    if N == 3:
        for i in range(3):
            for j in range(3):
                if not (i==1 and j==1):
                    screen[start[0]+i][start[1]+j] = "*"
    
    else:
        #col1
        next = N//3
        star(start,N//3)
        star((start[0]+next,start[1]),N//3)
        star((start[0]+next+next,start[1]),N//3)
        #col2
        star((start[0],start[1]+next),N//3)
        star((start[0]+next+next,start[1]+next),N//3)
        #col3
        star((start[0],start[1]+next+next),N//3)
        star((start[0]+next,start[1]+next+next),N//3)
        star((start[0]+next+next,start[1]+next+next),N//3)
        
N = int(input())

star((0,0),N)

for i in range(N):
    for j in range(N):
        print(screen[i][j],end='')
    print('')