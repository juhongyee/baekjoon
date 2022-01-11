n = int(input())
A = list(map(int,input().split()))

A.sort()

if(len(A) == 1):
    print("%d"%(A[0]**2))

else:
    B = A[0]*A[len(A)-1]
    print("%d"%(B))
