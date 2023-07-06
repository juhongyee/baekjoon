import sys

N,K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

num_list = [0]*(500000+1)
tree = [0]*(500000+1)

def sumation(i):
    ans = 0
    while i>0:
        ans += tree[i]
        i -= (i&-i)
    
    return ans

def update(i,num):
    while i<len(tree):
        tree[i] += num
        i += (i&-i)

count = 0
for idx,val in enumerate(arr):
    update(val,1)
    num_list[val] += 1
    num = (sumation(500000)-sumation(val))
    count += num
    
    if count>=K:
        target = arr[:idx-num]
        target.sort()
        print(*target,end = ' ')
        print(val,end =' ')
        target2 = arr[idx-num:idx+1]
        target2.sort()
        print(*target2)
        exit()

print(-1)