import math
#도로의 개수 N
N = int(input())

#사건의 개수
W = int(input())

dp = [[0,0] for i in range(W+1)]
event_list = []

#경찰차 1,2의 위치
loc_cop1 = [1,1]
loc_cop2 = [N,N]

#사건 입력
for i in range(W):
    event_list.append(list(map(int,input().split())))

for i in range(W):
    temp = event_list[i]
    
    #한 사건에 대해 두 경찰차로부터의 거리가 경찰차1이 더 크다면
    if(math.abs((temp[0]-loc_cop1[0]))+math.abs((temp[1]-loc_cop1[1]))>math.abs((temp[0]-loc_cop2[0]))+math.abs((temp[1]-loc_cop2[1]))):
        dp[i+1][1] = 2
        dp[i+1][0] = dp[i-1][0] + math.abs((temp[0]-loc_cop2[0]))+math.abs((temp[1]-loc_cop2[1]))
    
    #만약 같다면
    elif(math.abs((temp[0]-loc_cop1[0]))+math.abs((temp[1]-loc_cop1[1]))==math.abs((temp[0]-loc_cop2[0]))+math.abs((temp[1]-loc_cop2[1]))):
        decision = 0
        
        #그 다음 사건들을 쭉 관찰하자. 먼저 작게 되는 놈을 선택하자.
        for j in range(i+1,W):
            temp1 = event_list[j]
            if(math.abs((temp1[0]-loc_cop1[0]))+math.abs((temp1[1]-loc_cop1[1]))>math.abs((temp1[0]-loc_cop2[0]))+math.abs((temp1[1]-loc_cop2[1]))):
                decision = 2
                break
            else:
                decision = 1
                break
        
        if(decision == 2):
            dp[i+1][1] = 2
            dp[i+1][0] = dp[i-1][0] + math.abs((temp[0]-loc_cop2[0]))+math.abs((temp[1]-loc_cop2[1]))
    
        elif(decision == 1):
            dp[i+1][1] = 1
            dp[i+1][0] = dp[i-1][0] + math.abs((temp[0]-loc_cop1[0]))+math.abs((temp[1]-loc_cop1[1]))
    
    #만약 1이 더 작다면
    else:
        dp[i+1][1] = 1
        dp[i+1][0] = dp[i-1][0] + math.abs((temp[0]-loc_cop1[0]))+math.abs((temp[1]-loc_cop1[1]))
    
print(dp[W][0])