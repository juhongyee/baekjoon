import sys
N,M = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().split()))

tree.sort(reverse=1)

height = tree[0]
sum_tree = tree[0]

for i in range(1,len(tree)):
    if(sum_tree - tree[i]*i<M):
        sum_tree += tree[i]
        continue
    elif(sum_tree - tree[i]*i==M):
        height = tree[i]
        break
    else:
        height = (sum_tree-M)//i
        break

if(height == tree[0]):
    for_result = M - (sum_tree - tree[len(tree)-1]*len(tree))
    if(for_result%len(tree)==0):
        height = tree[len(tree)-1]-for_result//len(tree)
    else:
        height = tree[len(tree)-1]-for_result//len(tree)-1
print(height)
