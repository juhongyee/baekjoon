#동전 개수 및 가치의 합
n, k = map(int,input().split())

coin_list = [-1 for i in range(k+1)]
A = []

#동전 입력 n번

coin = 0
for i in range(0,n):
    coin = int(input())
    A.append(coin)

A.sort()
index = 0
for i in range(1,k+1):
  if(index<n-1):
    if(i-A[index+1]>=0):
      index = index + 1
  if(i-A[index]==0):
    coin_list[i] = 1
  else:
    min = 1000000
    for k1 in range(0,index+1):
      temp = coin_list[i-A[index-k1]]
      #print(temp)
      if(temp<min and temp!=-1):
        min = temp
    if(min!=1000000):
        coin_list[i] = min+1
    
print(coin_list[k])
