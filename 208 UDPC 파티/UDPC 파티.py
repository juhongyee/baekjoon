import sys

string = sys.stdin.readline().strip()

convert = {'U' : 0,'D' : 1,'P' : 2,'C' : 3}

num = [0]*2

for i in range(len(string)):
    cur = convert[string[i]]
    
    if(cur == 0 or cur==3):
        num[0] += 1
    
    elif(cur == 1 or cur ==2):
        num[1] += 1
if(num[1]==0):
    print('U')
    exit()
if(num[1]%2 == 1):
    if(num[0]<=num[1]//2+1):
        print('DP')
    else:
        print('UDP')
else:
    if(num[0]<=num[1]//2):
        print('DP')
    else:
        print('UDP')