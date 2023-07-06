N,K = map(int,input().split())

num_list = [0]*2**N

for i in range(2**N):
    count = 0
    now = i
    while now>0:
        if(now%2==1):
            count+=1
        now = now//2
        
    num_list[i] = count
count = 0

dict = {i:[] for i in range(2**N-1)}
for i in range(len(num_list)):
    dict[num_list[i]].append(i)

#N은 비트의 수 0~4 = 5, 0~3 = 4
for i in range(N//2+1):
    if(i!=N-i):
        for idx in range(len(dict[i])):
            count += 1
            if(count==K):
                print(dict[i][idx],dict[N-i][idx])
                count = 0
            else:
                print(dict[i][idx],dict[N-i][idx],end = ' ')
    else:
        for idx in range(0,len(dict[i]),2):
            count += 1
            if(count==K):
                print(dict[i][idx],dict[N-i][idx+1])
                count = 0
            else:
                print(dict[i][idx],dict[N-i][idx+1],end = ' ')