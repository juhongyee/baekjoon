import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

def f(x):
    sumation = 0
    for idx,val in enumerate(arr):
        sumation += abs(idx*x-val)

    return sumation

if(N == 1):
    print(0)
    exit()
left = 0
right = arr[N-1]

while left<=right:
    mid = (left+right)//2
    
    v_mid_l = f(mid-1)
    v_mid = f(mid)
    v_mid_r = f(mid+1)
    
    if (v_mid_l>v_mid and v_mid_r>v_mid):
        print(f(mid))
        exit()
    
    elif v_mid_l>v_mid>v_mid_r:
        left = mid+1
        
    elif v_mid_l<v_mid<v_mid_r:
        right = mid-1
