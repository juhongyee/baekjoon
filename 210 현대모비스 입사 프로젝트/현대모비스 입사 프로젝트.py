import sys
import math

N,K = map(int,sys.stdin.readline().split())

lecture = [0]*N

for i in range(N):
    lecture[i] = list(map(int,sys.stdin.readline().split()))
    
sum_list = [[],[],[]]

#조합 3개
comb = [(0,1),(0,2),(1,2)]

#2개의 합의 절댓값이 최대

for t in range(3):
    one = comb[t][0]
    two = comb[t][1]
    
    for i in range(N):
        val = lecture[i][one]+lecture[i][two]
        sum_list[t].append(val)

sum_list[0].sort(reverse=1)
sum_list[1].sort(reverse=1)
sum_list[2].sort(reverse=1)

sum_0 = 0
sum_1 = 0
sum_2 = 0

for i in range(K):
    sum_0 += sum_list[0][i]
    sum_1 += sum_list[1][i]
    sum_2 += sum_list[2][i]

print(max(sum_0,sum_1,sum_2))