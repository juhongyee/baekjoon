n = int(input())

for i in range(0,n):
    A = list(map(int,input().split()))
    if(A[0]<A[2]):
        print("No")
    else:
        if((A[0]-A[2])%2 != 0):#1x1이 ㄴ보다 많거나 같고 차가 짝수개
            print("No")
        else:
            if(A[1]==0):
                print("Yes")
            else:
                if(A[0] == 0 and A[2] == 0):
                    if(A[1]%2 != 0):
                        print("No")
                    else:
                        print("Yes")
                else:
                    print("Yes")

(A[0]-(A[2]-A[1]))%2 != 0
'''def block(A):
    if(A[0]<A[2]):
        print("No")
    else:
        if((A[0]-A[2])%2 != 0):#1x1이 ㄴ보다 많거나 같고 차가 짝수개
            print("No")
        else:
            if(A[1]==0):
                print("Yes")
            else:
                if(A[0] == 0 and A[2] == 0):
                    if(A[1]%2 != 0):
                        print("No")
                    else:
                        print("Yes")
                else:
                    if(A[1]<A[2]):
                        if((A[0]-(A[2]-A[1]))%2 != 0):
                            print("Yes")
                        else:
                            print("No")
                    else:
                        print("Yes")

for i in range(0,9):
    for j in range(0,9):
        for k in range(0,9):
            if(i == 0 and j==0 and k==0):
                continue
            else:
                if((i+2*j+3*k)%2==1):
                    continue
                else:
                    A = []
                    A.append(i)
                    A.append(j)
                    A.append(k)
                    print("%d %d %d"%(i,j,k))
                    block(A)'''
