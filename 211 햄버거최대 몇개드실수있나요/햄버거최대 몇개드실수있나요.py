import sys
import math
N,K,L = map(int,sys.stdin.readline().split())

mass = list(map(int,sys.stdin.readline().split()))

cola = list(map(int,sys.stdin.readline().split()))

cola_nuk = [0]*200000
colared = [0]*200000

for i in range(len(cola)):
    cola_nuk[cola[i]-1] += 1

colared[0] = cola_nuk[0]

for i in range(1,L):
    colared[i] = colared[i-1]+cola_nuk[i]
    
for i in range(L,N):
    colared[i] = colared[i-1]-cola_nuk[i-L]+cola_nuk[i]

sumation = 0

colared = colared[0:N]
colared.sort(reverse=1)
mass.sort(reverse=1)

for i in range(N):
    sumation += math.floor(mass[i]/(2**colared[i]))

print(sumation)