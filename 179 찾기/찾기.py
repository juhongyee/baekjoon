import sys
from collections import deque
#KMP로 풀 예정

def make_lps(pat,lps):
    lps[0] = 0
    
    j = 0 #이전 단계에서 경계의 다음 index
    
    for i in range(1,len(pat)):
        #i개 일치 상황, ABACABAAC 에서 1개 상황이면 A하나 겹침, 2개 상황이면 AB겹침
        while(pat[j]!=pat[i] and j>0): #같을 때까지 iter하고 j 옮김. 어떤 경계 다음의 index와 같을 떄까지
            j = lps[j] #lps는 개수이므로 그 경계 다음 index로 감. 왜 경계로 갈까?
            #ABACABABC에서 7개 겹치는 경우를 생각해보자. B를 확인했을 때 안맞으니 ABA를 확인한다는 것인데 그 ABA가 B 앞에도 존재한다.
            #이 때 ABA의 경계로 간다고하면 이는 앞의 ABA의 처음 A와 뒤 ABA의 끝 A가 맞다는 것과 같으므로 거기에 B를 붙이면 그것 또한 경계가 된다.
        
        #i개 일치 상황에 pat에서는 0~i-1이 일치하는 상황이고 pat[i]는 i+1번째인 i index보는 것(그니까 다음 걸 보는거임, 7개 겹치는 상황에 8번째를 채우는 것)
        if(pat[j] == pat[i]):#while을 통해 나온 어떤 경계의 값과 그 다음 값이 같음 그러면 경계를 이어붙이면 됨. 고로 j를 거기서 하나 늘리고
            j+=1 #index적으로 하나 올리고
            lps[i+1] = j #바로 위에서 하나 더 올린게 겹치는 개수

def KMPsearch(pat,txt):
    M = len(pat)
    N = len(txt)

    #거리와 일치 개수
    distance,cnt,idx = 0,0,0
    #LPS longest proper prefix which is suffix
    lps = [0 for i in range(M+1)]
    make_lps(pat,lps)
    count = 0
    memory_place = deque()
    
    while(1):
        #distance가 그 위치임
        #index는 그 위치부터 하나하나 check하는 것
        
        #허용범위를 벗어남
        if(distance)+M>N :
            break
        
        while(txt[idx+distance] == pat[cnt]):
            cnt += 1
            idx += 1
            
            if(cnt == M):
                memory_place.append(distance+1)
                break
        
        if(cnt==0):
            distance += 1
        else:
            distance += cnt-lps[cnt]
        idx = lps[cnt]
        cnt = lps[cnt]
    
    print(len(memory_place))
    for i in range(len(memory_place)):
        print(memory_place[i])
                
txt = sys.stdin.readline().rstrip('\n')
pat = sys.stdin.readline().rstrip('\n')
KMPsearch(pat,txt)