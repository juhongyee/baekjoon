import sys

N,A,B = map(int,sys.stdin.readline().split())

tile_1 = list(map(int,sys.stdin.readline().split()))
tile_2 = list(map(int,sys.stdin.readline().split()))

tile_1.sort(reverse=True)
tile_2.sort(reverse=True)

idx_1 = 0
idx_2 = 0

sumation = 0
now = 0

if(N%2==1):
    sumation += tile_1[idx_1]
    idx_1 += 1
    now += 1

while(idx_1+1 < A and idx_2 < B): #각 타일이 2개 1개 이상 남음
    if(N-now>1): #현재 한 칸 이상 남음
        #그러면 더 큰 것
        val = tile_1[idx_1] + tile_1[idx_1+1]
        
        if(tile_2[idx_2]>=val):
            sumation += tile_2[idx_2]
            idx_2 += 1
            now += 2
        else:
            sumation += val
            idx_1 += 2
            now += 2
    else: #딱 됨
        print(sumation)
        exit()
    
#tile1이 1개 남았거나 B를 다 씀 
if(idx_2==B): #B를 다 쓴 경우
    while(now<N):
        sumation += tile_1[idx_1] 
        idx_1 += 1
        now += 1
    print(sumation)

else:
    while(now<N):
        sumation += tile_2[idx_2] 
        idx_2 += 1
        now += 2
    print(sumation)