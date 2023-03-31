import sys
import math

N = int(sys.stdin.readline())

for i in range(N):
    A,B,C,D = map(int,sys.stdin.readline().split())
    
    range_iter = int(math.sqrt(abs(D)))
    for i in range(0,range_iter+10):
        j = -1*i
        if(A*(i**3)+B*(i**2)+C*i+D==0):
            alpha = i
            break
        elif(A*(j**3)+B*(j**2)+C*j+D==0):
            alpha = j
            break
    a = A
    b = A*alpha+B
    c = C+b*alpha
    
    in_root = b*b-4*a*c
    
    if(in_root < 0):
        print("{:f}".format(float(alpha)))
        
    elif(in_root == 0):
        result = -1*b/(2*A)
        if(result==alpha):
            print("{}".format(result))
        else:
            print("{} {}".format(min(result,alpha),max(result,alpha)))
    
    else: 
        root_1 = (-1*b+math.sqrt(in_root))/(2*a)
        root_2 = (-1*b-math.sqrt(in_root))/(2*a)
        
        ans = [root_1,root_2,float(alpha)]
        
        ans.sort()
        
        if(ans[0] == ans[1]):
            print("{} {}".format(ans[0],ans[2]))
        elif(ans[1] == ans[2]):
            print("{} {}".format(ans[0],ans[1]))
        else:
            print("{} {} {}".format(ans[0],ans[1],ans[2]))