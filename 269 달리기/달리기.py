import sys

def sumation(tree,i):
    ans = 0
    while i>0:
        ans += tree[i]
        i -= (i&-i)
    
    return ans

def update(tree,i,num):
    while i<len(tree):
        tree[i] += num
        i += (i&-i)
    
N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

for_map = sorted(arr)
#정렬되어 있음
#예를 들어 2를 0으로 mapping(가장 처음이 2라면)
mapping = {}
for idx in range(1,len(arr)+1):
    mapping[for_map[idx-1]] = idx

for idx in range(len(arr)):
    arr[idx] = mapping[arr[idx]]

#이제 좌표 압축이 완료됨.
#Fenwick tree를 통해 값을 계산
num_front = [0]*500000
tree = [0]*(500000+1)

for i in range(1,N+1):
    if(i!=1):
        print(sumation(tree,500000)-sumation(tree,arr[i-1])+1)
    else:
        print(1)
    update(tree,arr[i-1],1)
    