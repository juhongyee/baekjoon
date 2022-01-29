import sys
n = int(input()) #수행해야 하는 연산 개수

def add(S,x):
    temp = 0b1<<(x-1) #1을 밀어 그리고 그냥 or
    return S|temp

def remove(S,x):
    temp = ~(0b1<<(x-1)) # 1밀고 not 시키고 바로 and
    return S&temp

def check(S,x):
    temp = 0b1<<(x-1) #1밀어보고 or 해서 0이면 없어
    if(temp&S == 0):
        return 0
    else:
        return 1
    
def toggle(S,x):
    if(check(S,x)): #있다면
        S = remove(S,x)
    else:
        S = add(S,x)

    return S
def a11():

    return 0b11111111111111111111

def empty():
    return 0b0
    
S = 0b0
for i in range(0,n):

    command = sys.stdin.readline().split()

    if(command[0] == 'add'):
        S = add(S,int(command[1]))
        
    elif(command[0] == 'remove'):
        S = remove(S,int(command[1]))
        
    elif(command[0] == 'check'):
        print(check(S,int(command[1])))

    elif(command[0] == 'toggle'):
        S = toggle(S,int(command[1]))
    
    elif(command[0] == 'all'):
        S = a11()

    else:
        S = empty()

         
