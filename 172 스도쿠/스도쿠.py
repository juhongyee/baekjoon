def possible_check(empty,game):
    dic = {}
    
    for target in empty:
        dic[target] = []
        #x행 y열 직사각형
        x = target[0]//3
        y = target[1]//3
        
        subtraction = [1 for i in range(10)]
        subtraction[0] = 0
        
        #game에 있는 값은 0으로 만들어줌.
        for i in range(x*3,x*3+3):
            for j in range(y*3,y*3+3):
                subtraction[game[i][j]] = 0
        
        #행 제거
        for i in range(9):
            subtraction[game[i][target[1]]] = 0
        
        for j in range(9):
            subtraction[game[target[0]][j]] = 0
        
        #game에 없는 값만 subtraction에 1로 남음 그 값을 저장      
        for i in range(10):
            if(subtraction[i] != 0):
                dic[target].append(i)
    
    return dic

def check(game,val,coordinate):
    x = coordinate[0]//3
    y = coordinate[1]//3
    
    mem = [0,0,0,0,0,0,0,0,0,0]
    #mem = [for i in range(10)] 쓰지마라 3번이나 쓰니까 시간 개오래걸림
    
    #정사각형 valid check
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if(game[i][j]!=0):
                if(mem[game[i][j]]==0):
                    mem[game[i][j]] += 1
                else:
                    return False
    #line check
    #행 check
    mem = [0,0,0,0,0,0,0,0,0,0]
    for j in range(9):
        if(game[coordinate[0]][j]!=0):
            if(mem[game[coordinate[0]][j]]==0):
                mem[game[coordinate[0]][j]] += 1
            else:
                return False
    #열 check
    mem = [0,0,0,0,0,0,0,0,0,0]
    for i in range(9):
        if(game[i][coordinate[1]]!=0):
            if(mem[game[i][coordinate[1]]]==0):
                mem[game[i][coordinate[1]]] += 1
            else:
                return False          
    return True

def back_tracking(idx,empty,dic,fin):
    
    if(idx == fin):
        #가능한 값들에 관해 반복문
        for val in dic[empty[idx]]:
            #넣어보고
            game[empty[idx][0]][empty[idx][1]] = val
            #check를 만족하면
            if(check(game,val,empty[idx])):
                for i in range(9):
                    for j in range(9):
                        print(game[i][j],end='')
                        if(j!=8):
                            print(' ',end='')
                        else:
                            print('')
                
                exit()
        game[empty[idx][0]][empty[idx][1]] = 0
        
    else:
        for val in dic[empty[idx]]:
            game[empty[idx][0]][empty[idx][1]] = val
            if(check(game,val,empty[idx])):
                back_tracking(idx+1,empty,dic,fin)
        game[empty[idx][0]][empty[idx][1]] = 0
    

game = [0 for i in range(9)]

for i in range(9):
    game[i] = list(map(int,input().split()))

#스도쿠의 빈칸확인
empty = []

for i in range(9):
    for j in range(9):
        if(not game[i][j]):
            empty.append((i,j))

dic = possible_check(empty,game)
fin = len(empty)-1
back_tracking(0,empty,dic,fin)