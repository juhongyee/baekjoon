N = int(input(""))

n = 0
k = 0
listmin = list()

for n in range(0,1001,1):

    for k in range(0,1335,1):

        t = 5*n + 3*k

        if N == t :
            l = n + k
            listmin.append(l)


if len(listmin) == 0 :
    print(-1)

else :
    print(min(listmin))
