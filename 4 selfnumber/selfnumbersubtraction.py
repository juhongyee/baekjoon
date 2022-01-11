a = 0
b = 0
c = 0
d = 1
fd = list()
n = 1
f = 0
fd2 = list()
k = 0
for f in range(0,10,1) :

    for a in range(0,10,1) :

        for b in range(0,10,1) :

            for c in range(0,10,1) :

                for d in range(0,10,1) :

                    e = 10001*f+1001*a+101*b+11*c+2*d

                    fd.append(e)
            

while 1 :

    if fd.count(n) == 0 :

        fd2.append(n)

    n = n+1

    if n == 80000 :
        break

while 1:
    print(fd2[k+1] - fd2[k])

    k = k+1

    if k == 7600 :
        break
    
