#n 입력

n = int(input())

A = [0 for i in range(n+1)]
A[0] = 1

B = []
ele2 = 1
while(1):
    B.append(ele2)
    ele2 *= 2

    if(ele2>n):
        break

for i in range(0,len(B)):
    for j in range(B[i],n+1):
        A[j] += A[j-B[i]]
        A[j] %= 1000000000
print(A[n]%1000000000)
