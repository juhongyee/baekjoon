def cal_len(val):
    start = 1
    end = 9
    len = 1
    ans = 0
    while (start<=val):
        if(end>val):
            end = val
        
        ans += (end-start+1)*len
        len += 1
        start *= 10
        end = start*10-1
    
    return ans


n,k = map(int,input().split())
start = 0
end = n

while start<end: #lower bound를 구하자.
    mid = (start+end)//2
    temp = cal_len(mid)
    if(temp<k):
        start = mid+1
    else:
        end = mid

a = cal_len(end) - k

if(a+k <= k):
   if(a==0):
       print(end%10)
   else:
       print(-1)
else: 
    if(a==0):
        print(end%10)
    else:
        k = str(end)
        print(k[-1+(-1*a)])
    
    