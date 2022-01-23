import math
#재료의 개수
N = int(input())

food_list = [[0 for i in range(2)] for j in range(N)]

for i in range(0,N):
    food_list[i] = list(map(int,input().split()))

different_min = 0


for i in range(1,2**(N)):
    product = 1
    sum = 0
    A = bin(i)[2:]
    B = ['O' for i in range(N-len(A))]
    B = "".join(B)
    A = B+A
    for j in range(0,N):
        if(A[j]=='1'):
            product *= food_list[j][0]
            sum += food_list[j][1]
    #print(A)
    #print(abs(product-sum))
    if(i==1):
        different_min = abs(product-sum)
    else:
        if(different_min>abs(product-sum)):
            different_min = abs(product-sum)

print(different_min)
            
                   
    
