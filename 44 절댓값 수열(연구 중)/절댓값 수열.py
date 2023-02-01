from collections import deque
import sys

def absol(first,second,interval):
    if(first<second and first!=0 and second!= 0):
        temp = first
        first = second
        second = temp
    if(first!=0 and second!= 0):
        big_num = first//second
        small_num = (first//second-1)//2+1
        if(interval):
            interval.append(interval[-1]+big_num+small_num)
        else:
            interval.append(big_num+small_num)
        
        return absol(second,first%second,interval)
    
    else:
        return first

# def result_print(f,s,N):
#     if(N==0):
        
#     else:
#         ()

def calcul(first,second,iter):
    s_1 = first
    s_2 = second
    temp = 0
    for i in range(iter-1):
        temp = s_2
        s_2 = abs(s_2-s_1)
        s_1 = temp
    print(s_2)
    
first,second,N = map(int,sys.stdin.readline().split())

Q = []
for i in range(N):
    Q.append(int(sys.stdin.readline()))

interval = []

gcd = absol(first,second,interval)

detect = 0
if(calcul(first,second,interval[-1]+1)==0):
    detect = 1
else:
    detect = 0
    
for i in range(len(Q)):
    if(interval):
        if(Q[i] == 0):
            print(first)
        elif(Q[i] == 1):
            print(second)
        elif(Q[i]<=interval[-1]):
            calcul(first,second,Q[i])
                    
        else:
            if (Q[i]-(interval[-1]+1))%3 == detect:
                print(0)
            else:
                print(gcd)
    else:
        if(first==0):
            if(Q[i]%3==0):
                print(first)
            else:
                print(second)
        else:
            if(Q[i]%3==1):
                print(second)#second가 0
            else:
                print(first)