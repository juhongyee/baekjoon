def cutting(A,start,end,start2,end2,color):
    if(start==end):
        color[A[start][start2]] += 1
        print(1)
        return 0
    for i in range(start,end+1):
        for j in range(start2,end2+1):
            if(A[i][j]!=A[start][start2]):
                cutting(A,start,end//2,start2,end2//2,color)
                print(1,color)
                cutting(A,end//2+1,end,start2,end2//2,color)
                print(2,color)
                cutting(A,start,end//2,end2//2+1,end2,color)
                print(3,color)
                cutting(A,end//2+1,end,end2//2+1,end2,color)
                print(4,color)
                return 0
    color[A[start][start2]] += 1
    #print(1)
    return 0

#색종이 한 변의 길이
N = int(input())

color = [0,0]

color_paper = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(1,N+1):
    color_paper[i] = [0]+list(map(int,input().split()))
#print(color_paper)
cutting(color_paper,1,N,1,N,color)
print(color[0])
print(color[1])