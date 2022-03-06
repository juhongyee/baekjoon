import math
import sys
import time

#start = time.time()
A = [1 for i in range(1000001)]

for i in range(2,1000001):
    for j in range(i,1000001,i):
        A[j] += i
for i in range(2,1000001):
    A[i] = A[i-1]+A[i]
#test_case 개수 T
#print("time :", time.time() - start)
T = int(input())

for i in range(T):
    N = int(sys.stdin.readline())
    print(A[N])
