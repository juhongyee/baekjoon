import sys

T = int(input())

for i in range(T):
    A = list(sys.stdin.readline().strip())
    complete = True
    mclose = 0
    for j in range(len(A)):
        temp = A.pop()

        if(temp == ')'):
            mclose += 1
            

        elif(temp == '('):
            mclose -= 1

        if(mclose<0):
            print("NO")
            complete =  False
            break
    
    if(complete):
        if(mclose==0):
            print("YES")
        else:
            print("NO")
    

    
