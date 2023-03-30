import sys
import math

def dist(p1,p2):
    x = (p1[0]-p2[0])**2
    y = (p1[1]-p2[1])**2
    
    return x+y

def near_dist(point_list,start,end):
    #only 2 points are in the set.
    if(end-start+1==2):
        return dist(point_list[start],point_list[end])
    
    #3 points are in the set.
    elif(end-start+1==3):
        p1 = point_list[start]
        p2 = point_list[start+1]
        p3 = point_list[start+2]
        
        return min(dist(p1,p2),dist(p1,p3),dist(p2,p3))
    
    cut = (start+end)//2
    d1 = near_dist(point_list,start,cut)
    d2 = near_dist(point_list,cut+1,end)
    
    min_d = min(d1,d2)
    
    #cut부터 min_d보다 작은 x값의 차를 가진 영역 left~right
    left = cut
    right = cut+1
    cut_val = point_list[cut][0]
    
    target = []
    # while(1):
    #     #left,right가 0이상에서 만약 지금까지 최소 거리 이내면 index를 1씩 옮김.
    #     if((cut_val-point_list[left][0])**2<=min_d and left>0):
    #         left -= 1
    #     if((cut_val-point_list[right][0])**2<=min_d and right<end):
    #         right += 1

    #     #0이나 끝에 도달했거나 거리가 현재까지 최소 이상이면 break
    #     if((left==0 or (cut_val-point_list[left][0])**2>min_d) and (right==end or (cut_val-point_list[right][0])**2>min_d)):
    #         break
    
    for i in range(start,end+1):
        #cut이 중간 점
        if((point_list[cut][0]-point_list[i][0])**2<min_d):
            target.append(point_list[i])
    
    target.sort(key=lambda x:x[1])
    
    #겹치지 않게 pair를 세는법
    for i in range(len(target)-1):
        for j in range(i+1,len(target)):
            #사실 각각 나눠서 하면 더 최적화도 가능할듯
            if((target[i][1]-target[j][1])**2<min_d):
                min_d = min(min_d,dist(target[i],target[j]))
            else:
                break
    
    return min_d

n = int(sys.stdin.readline())

point_list = []
#point 입력
for i in range(n):
    point_list.append(tuple(map(int,sys.stdin.readline().split())))

#한 번에 정렬하면 안됨.
point_list.sort(key=lambda x:(x[0]))

print(near_dist(point_list,0,len(point_list)-1))