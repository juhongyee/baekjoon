import sys

N,M = map(int,sys.stdin.readline().split())

count = 0
picture = [0]*N

for i in range(N):
    picture[i] = sys.stdin.readline().split()

for line in picture:
    check = ''.join(line)
    check = check.split('0')

    for string in check:
        mode_num = [0,0,0]

        if(len(string)>=1):
            mode = string[0]
            mode_num[int(mode)] += 1
            
            for i in range(1,len(string)):
                if(mode == string[i]):
                    continue
                else:
                    mode = string[i]
                    mode_num[int(mode)] += 1
                
            count += min(mode_num[1],mode_num[2])+1

print(count)