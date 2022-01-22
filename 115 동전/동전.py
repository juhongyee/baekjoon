#test_case의 개수
T = int(input())

for i in range(0,T):
    coin = int(input())

    A = list(map(int,input().split()))

    value = int(input())

    coin_list = [0 for i in range(value+1)]

    coin_list[0] = 1

    for i in range(0,coin):
        if(A[i]<=value):
            for j in range(A[i],value+1):
                coin_list[j] += coin_list[j-A[i]]

    print(coin_list[value])
