n,p,k,d = map(int,input().split())

if(d!=1):
    if(p<(d*(d-1)//2)):
        print("Wrong information")
        exit()
    now = d-2
    print(d-1+(p-(d*(d-1)//2)))

    for i in range(n-1):
        if(now-i>0):
            print(now-i)
        else:
            print(0)

else:
    #다 똑같이 나눠줘야 함.
    if(p<d): #못나눠 줌
        print("Wrong information")
        exit()
    else:
        q = p//k
        r = p%k
        
        if(r>0):
            if(k==n):
                print("Wrong information")
                exit()

        for i in range(k):
            print(q)
        print(r)
        for i in range(n-k-1):
            print(0)