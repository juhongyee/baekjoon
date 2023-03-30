
N,K = map(int,input().split())

remainder = K

count = 0
cnt = N-1

while(remainder>cnt):
    count += 1
    remainder -= cnt
    cnt -= 1

for i in range(count):
    print(N-i,end = ' ')

print(remainder+1,end = ' ')

for i in range(1,remainder+1):
    print(i,end = ' ')
    
for i in range(remainder+2,N-count+1):
    if(i != N-count):
        print(i,end = ' ')
    else:
        print(i)
