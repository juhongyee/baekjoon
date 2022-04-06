import sys

def uclid(a,b):
    if(b==0):
        return a
    else:
        return uclid(b,a%b)

#testcase의 개수 C
C = int(sys.stdin.readline())

count = [0 for i in range(1001)]
count[1] = 3
count[2] = 5

for i in range(3,1001):
    case_count = 0
    for j in range(1,i):
        if(uclid(i,j)==1):
            case_count+=1
    case_count *= 2

    count[i] = count[i-1]+case_count

for i in range(C):
    a = int(sys.stdin.readline())
    print(count[a])

