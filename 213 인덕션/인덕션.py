import sys
import math

sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())

cuisine = [0]+list(map(int,sys.stdin.readline().split()))
all_sum = math.inf

def dist(i1,i2,i3,idx,dis):
    obj = cuisine[idx]
    
    if(idx==N):
        global all_sum
        d1 = min(abs(obj-i1),min(abs(0-i1)+9-obj+1,abs(9-i1)+obj+1))
        d2 = min(abs(obj-i2),min(abs(0-i2)+9-obj+1,abs(9-i2)+obj+1))
        d3 = min(abs(obj-i3),min(abs(0-i3)+9-obj+1,abs(9-i3)+obj+1))
        
        distance = dis+min(d1,d2,d3)
        if(distance<all_sum):
            all_sum = distance
        
        return
    
    #단순거리 vs 왼쪽 끝으로 돌아가기 오른쪽 끝으로 돌아가기 greedy
    d1 = min(abs(obj-i1),min(abs(0-i1)+9-obj+1,abs(9-i1)+obj+1))
    d2 = min(abs(obj-i2),min(abs(0-i2)+9-obj+1,abs(9-i2)+obj+1))
    d3 = min(abs(obj-i3),min(abs(0-i3)+9-obj+1,abs(9-i3)+obj+1))
    
    #대칭성을 이용
    # 5 0 0/0 5 0/0 0 5는 사실상 같음.
    arr1 = [obj,i2,i3]
    arr2 = [i1,obj,i3]
    arr3 = [i1,i2,obj]
    
    arr1.sort()
    arr2.sort()
    arr3.sort()
    
    r1,r2,r3 = 25000,25000,25000
    
    minimum = min(d1,d2,d3)
    
    if(d1==d2 and d2==d3):
        if(arr1==arr2 and arr2==arr3):
            dist(obj,i2,i3,idx+1,dis+d1)
        elif(arr1==arr2):
            dist(obj,i2,i3,idx+1,dis+d1)
            dist(i1,i2,obj,idx+1,dis+d3)
        elif(arr1==arr3):
            dist(obj,i2,i3,idx+1,dis+d1)
            dist(i1,obj,i3,idx+1,dis+d2)
        elif(arr2==arr3):
            dist(obj,i2,i3,idx+1,dis+d1)
            dist(i1,obj,i3,idx+1,dis+d2)
        else:
            dist(obj,i2,i3,idx+1,dis+d1)
            dist(i1,obj,i3,idx+1,dis+d2)
            dist(i1,i2,obj,idx+1,dis+d3)
    
    elif(d1==d2==minimum):
        if(arr1 == arr2):
            dist(obj,i2,i3,idx+1,dis+d1)
        else:
            dist(obj,i2,i3,idx+1,dis+d1)
            dist(i1,obj,i3,idx+1,dis+d2)
    
    elif(d1==d3==minimum):
        if(arr1 == arr3):
            dist(obj,i2,i3,idx+1,dis+d1)
        else:    
            dist(obj,i2,i3,idx+1,dis+d1)
            dist(i1,i2,obj,idx+1,dis+d3)
    
    elif(d2==d3==minimum):
        if(arr2 == arr3):
            dist(i1,obj,i3,idx+1,dis+d2)
        else:
            dist(i1,obj,i3,idx+1,dis+d2)
            dist(i1,i2,obj,idx+1,dis+d3)
    else:
        
        if(minimum==d1):
            dist(obj,i2,i3,idx+1,dis+d1)
        elif(minimum==d2):
            dist(i1,obj,i3,idx+1,dis+d2)
        else:
            dist(i1,i2,obj,idx+1,dis+d3)

dist(0,0,0,1,0)

print(all_sum)