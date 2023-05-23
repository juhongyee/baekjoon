import sys
N = int(sys.stdin.readline())

height = list(map(int,sys.stdin.readline().split()))

count = 0
idx = 0
flag = True
while(idx!=len(height)):
    if(flag):
        count += 1
        flag = False
        idx += 1
    else:
        if(height[idx-1]>height[idx]):
            idx+=1
        else:
            flag = True

print(count)