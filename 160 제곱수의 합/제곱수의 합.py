import math
import numbers
#입력
a = int(input())

dp = list(range(0,100000))
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,a+1):
    min_num = dp[i]
    if(not math.sqrt(i).is_integer()):
        for j in range(1,i//2+1):
            min_num = min(dp[i],dp[j]+dp[i-j])
            if(dp[i]>min_num):
                dp[i] = min_num
    else:
        dp[i] = 1

print(dp[a])

#시간초과코드
# import math
# import numbers
# #입력
# a = int(input())

# dp = list(range(0,a+1))
# dp = list(map(lambda x: 1 if(math.sqrt(x).is_integer()) else x,dp))
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# for i in range(4,a+1):
#     min_num = dp[i]
#     for j in range(1,i//2+1):
#         min_num = min(dp[i],dp[j]+dp[i-j])
#         if(dp[i]>min_num):
#             dp[i] = min_num

# print(dp[a])