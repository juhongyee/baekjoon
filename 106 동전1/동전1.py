#동전 개수 및 가치의 합
n, k = map(int,input().split())

coin_list = [0 for i in range(k+1)]
A = []

#동전 입력 n번

coin = 0
for i in range(0,n):
    coin = int(input())
    A.append(coin)

#동전 목록 sort
A.sort()
coin_list[0] = 1

for i in range(0,len(A)):
    if(A[i]<=k): #A가 k보다 큰 경우는 제외
        for j in range(A[i],k+1):
            coin_list[j] += coin_list[j-A[i]]

print(coin_list[k])
