N = int(input())

data_list = []

for i in range(N):
    data_list.append(input())

data_list2 = []
for i in range(N):
    data = (data_list[i],len(data_list[i]))
    data_list2.append(data)

data_list2.sort(lambda x: (x[0],x[1]))

for i in range(N):
    print(data_list2[i][0])