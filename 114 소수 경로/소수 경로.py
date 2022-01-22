from queue import Queue
def sieve():
    erato = [1 for i in range(10001)]
    erato[0] = 0
    erato[1] = 0

    for i in range(2,10001):
        if(erato[i] == 1):
            for j in range(2*i,10001,i):
                erato[j] = 0

    return erato
#join은 list를 하나하나 합쳐서 str로 반환
def prime(num1,erato,q1):
    temp = list(num1)
    for i in range(0,9):
        temp = list(num1)
        temp[0] = chr(49+i)
        S = ''.join(temp)
        if(erato[int(S)] and not visited[int(S)]):
            q1.put(S)
            visited[int(S)] = True
    for i in range(0,10):
        temp = list(num1)
        temp[1] = chr(48+i)
        S = ''.join(temp)
        if(erato[int(S)] and not visited[int(S)]):
            q1.put(S)
            visited[int(S)] = True
    for i in range(0,10):
        temp = list(num1)
        temp[2] = chr(48+i)
        S = ''.join(temp)
        if(erato[int(S)] and not visited[int(S)]):
            q1.put(S)
            visited[int(S)] = True
    for i in range(0,10):
        temp = list(num1)
        temp[3] = chr(48+i)
        S = ''.join(temp)
        if(erato[int(S)] and not visited[int(S)]):
            q1.put(S)
            visited[int(S)] = True
            
erato = sieve()

#test_case의 수
T = int(input())

for i in range(0,T):
    count = 1 #개수
    complite = False
    q1 = Queue() #queue를 하나 선언
    q2 = Queue()
    #수 입력
    num1,num2 = input().split()
    visited = [0 for i in range(10001)]

    if(num1==num2):
        print("0")
        continue
    prime(num1,erato,q1)
    while(not complite):
        if(count%2==1):
            while(not q1.empty()):
                temp = q1.get()
                #print(temp)
                if(temp == num2):
                    complite = True
                    print(count)
                prime(temp,erato,q2)

            count += 1
        else:
            while(not q2.empty()):
                temp = q2.get()
                #print(temp)
                if(temp == num2):
                    complite = True
                    print(count)
                prime(temp,erato,q1)

            count += 1
