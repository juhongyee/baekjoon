p,seed,x1,x2 = map(int,input().split())

a = 0
b = 0

#x1-x2를 저장
differ = x1-x2
if(differ<0):
    while(differ<0):
        differ += p    

for i in range(p):
    if(((seed-x1)*i)%p == differ):
        a = i
        for j in range(p):
            if((a*seed+j)%p == x1):
                b = j
                break
        break

print(a,b)