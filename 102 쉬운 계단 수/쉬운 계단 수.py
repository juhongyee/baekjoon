#각 자릿수의  개수를 저장하는 array
memories = [[0 for col in range(10)] for row in range(101)]

memories[1] = [0,1,1,1,1,1,1,1,1,1]

n = int(input())

for i in range(2,n+1):
    for j in range(0,10):
        if(j==0):
            memories[i][0] = +memories[i-1][1]
        elif(j==9):
            memories[i][9] = memories[i-1][8]
        else:
            memories[i][j] = memories[i-1][j-1]+memories[i-1][j+1]

sum = 0
for i in range(0,10):
    sum += memories[n][i]
    sum = sum%1000000000

print(sum)
