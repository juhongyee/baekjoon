import sys

def Bsearch(low,high,value,A):
    while(low<high):
        mid = (low+high)//2
        
        if(value<=A[mid]):
            high = mid
        else:
            low = mid+1
    
    return low



#수열 길이와 수열 입력
N = int(input())
A = list(map(int,sys.stdin.readline().split()))

#i번째 길이이며 D[i]로 끝나는 부분수열이 존재함을 알려주는 수열 D 선언
D = [0 for i in range(N)]
d_index = 0
for i in range(0,N):
    k = Bsearch(0,d_index,A[i],D)
    D[k] = A[i]
    if(k==d_index):
        d_index+=1

print(d_index)
