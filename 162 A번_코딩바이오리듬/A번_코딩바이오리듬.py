import sys
import math

def convert(target,me):
    value1 = 0
    value2 = 0
    value3 = 0
    
    for i in range(4):
        value1 += math.pow((int(target[i])-int(me[i])),2)
    
    for i in range(4,6):
        value2 += math.pow((int(target[i])-int(me[i])),2)
        
    for i in range(6,8):
        value3 += math.pow((int(target[i])-int(me[i])),2)
        
    return (value1*value2*value3,int(target))


me = input()
max = (0,math.inf)

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().strip())

for i in range(N):
    cal = arr[i]
    cal = convert(cal,me)
    
    if(cal[0]>max[0]):
            max = cal
    elif(cal[0] == max[0]):
        if(cal[1]<max[1]):
            max = cal

print(max[1])
