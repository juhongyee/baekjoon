def reculsive_dp(A,value,index,coin_list):

    if(index==-1):
        return -1 #더 이상 빼볼 게 없음
    elif(coin_list[value] != -1):#최소치 일 경우
        return coin_list[value]
    else:
        if(A[index]>value):#빼는 값이 더 큰 경우
            return reculsive_dp(A,value,index-1,coin_list)
        else:
            minimum = 100001
            for i in range(index,-1,-1):
                temp = reculsive_dp(A,value-A[i],index,coin_list)
                if(minimum>temp):
                    minimum = temp
            if(minimum!=-1):
                coin_list[value] = minimum+1
                return minimum+1
            else:
                return -1
        
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
    return high

#동전 개수 및 가치의 합
n, k = map(int,input().split())

coin_list = [-1 for i in range(100001)]
A = []

#동전 입력 n번

coin = 0
for i in range(0,n):
    coin = int(input())
    if(coin<=10000):
        A.append(coin)
        coin_list[coin] = 1
A.sort()
print(reculsive_dp(A,k,binary_search(A,k),coin_list))

            
    
