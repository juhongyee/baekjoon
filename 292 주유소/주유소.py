import sys

N = int(sys.stdin.readline())

dist = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

min_index = [0]
for i in range(1,N):
    if(price[min_index[-1]]>price[i]):
        min_index.append(i)

ans = 0
for i,idx in enumerate(min_index):
    cur_p = price[idx]
    cur_dist = 0
    if(i==len(min_index)-1):
        for j in range(idx,len(dist)):
            cur_dist += dist[j]
    
    else:
        for j in range(idx,min_index[i+1]):
            cur_dist += dist[j]
    
    ans+=cur_p*cur_dist
    
print(ans)