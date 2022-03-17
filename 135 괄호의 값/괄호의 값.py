import sys

def cal(A,sum,close):
    if(len(A) == 0):
        if(close[0] == 0 and close[1] == 0):
            return sum
        else:
            print(0)
            sys.exit(0)
        
    temp = A.pop()
    if(temp == ')'):
        if(A[-1] != '('):
            return 2*cal(A,sum,close)
        else:
            return 
    elif(temp == '('):
        close[0] -= 1
        

A = list(sys.stdin.readline().strip())
close = [0,0]


    
            
        
    
