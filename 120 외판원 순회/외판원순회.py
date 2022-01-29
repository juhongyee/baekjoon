import math
def Isin(S,i):
    if((S&(1<<i-1))!=0):
        return True
    else:
        return False

def diff(S,j):
    t = 1<<(j-1)
    return (S&(~t))

def count(S,n):
    count = 0
    for i in range(n):#맨 마지막 자리까지
        if((S&(1<<i))!= 0):#and연산은 0을 하면 없얘고 1을 하면 그대로 냅둠.
            count += 1
    return count

def travel(W,n):
    size = pow(2,n)
    D = [[0 for i in range(size)] for j in range(n+1)]
    
    for i in range(2,n+1):
        D[i][0] = W[i][1]

    for A in range(1,n-1):#n-2번의 연산을 거쳐야 함.
        for i in range(1,size): #비트마스킹, 모든 집합을 순회하는 것
            if(count(i,n) == A): #n개의 집합에 관하므로 (i,n) , 그 집합의 개수가 현재 사이클과 같음.
                for j in range(2,n+1):
                    if(not Isin(i,j) and not Isin(i,1)):#사이 지나가는 집합에 j가 속해서는 안 됨.
                        D[j][i] = minimum(W,D,j,i)
                        #print(j,i,D[j][i],A)
    i = size-1-1 #n=4일 때 size는 16 15가 1111이니까 -1, 1일 때는 제외하고 2 3 4가 1인 상태이므로 다시 -1
    D[1][i] = minimum(W,D,1,i) #마지막 1에 관해 결정.

    return D[1][i]
                        
def minimum(W,D,j,i):
    minValue = math.inf
    n = len(W) -1
    for k in range(2,n+1):
        if(Isin(i,k)): #집합에 k가 속해 있기만 하면
            m = W[j][k]+D[k][diff(i,k)]
            '''print(k)
            print(diff(i,k))
            print(W[j][k])
            print(D[k][diff(i,k)])'''
            if(minValue>m):
                minValue =m

    return minValue
            

    
n = int(input())

W = [[] for i in range(n+1)]

for i in range(n):
    W[i+1] = [0]+list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(0,n+1):
        if(W[i][j] == 0):
            W[i][j] = math.inf
print(travel(W,n))
