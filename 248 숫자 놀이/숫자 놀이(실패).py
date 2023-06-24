import sys

# N = int(input())

# arr = list(map(int,sys.stdin.readline().split()))

N = 4

def number(arr):
    arr = list(map(lambda x:(x,x%N),arr))

    dict = {x : [] for x in range(N)}

    for i in range(len(arr)):
        dict[arr[i][1]].append(arr[i][0])

    key_list = list(dict.keys())
    key_list.sort(reverse = True)

    ans = []

    for key in key_list:
        if(key<N//2):
            break
        
        num = min(len(dict[key]),len(dict[N-key]))
        
        if(key != N-key):
            for i in range(num):
                ans.append(dict[key][i])
                ans.append(dict[N-key][i])
        else:
            for i in range(num-num%2):
                ans.append(dict[key][i])

    for i in range(len(dict[0])):
        ans.append(0)

    return ans
# ans = test
# if(len(ans)<N):
#     print('-1')
# else:
#     for i in range(N):
#         print(ans[i][0],end=' ')

# for x1 in range(10):
#     for x2 in range(10):
#         for x3 in range(10):
#             for x4 in range(10):
#                 for x5 in range(10):
#                     for x6 in range(10):
#                         for x7 in range(10):
#                             arr = [x1,x2,x3,x4,x5,x6,x7]
#                             ans = number(arr)
                            
#                             if sum(ans[0:N])%N != 0 or len(ans)<N:
#                                 print(arr)
#                                 print(ans)
#                                 exit()