import sys
from collections import deque
def make_lps(pat,lps):
    lps[0] = 0
    
    j = 0
    
    for i in range(1,len(pat)):
        
        while pat[j]!=pat[i] and j>0:
            j = lps[j]
        
        if(pat[j]==pat[i]):
            j+=1
            lps[i+1] = j
            
def KMPsearch(pat,txt):
    M = len(pat)
    N = len(txt)

    #거리와 일치 개수
    distance,cnt,idx = 1,0,0
    #LPS longest proper prefix which is suffix
    lps = [0 for i in range(M+1)]
    make_lps(pat,lps)
    count = 0
    memory_place = deque()
    
    while(1):
        if(distance)+M>N-1 :
            break
        
        while(txt[idx+distance] == pat[cnt]):
            cnt += 1
            idx += 1
            
            if(cnt == M):
                return 1
        
        if(cnt==0):
            distance += 1
        else:
            distance += cnt-lps[cnt]
        idx = lps[cnt]
        cnt = lps[cnt]

def post_pre(txt):
    lps = [0 for i in range(len(txt)+1)]
    make_lps(txt,lps)
    if(lps[len(txt)] == 0):
        print(-1)
        exit()
    return lps

def kameleon(txt):
    fix = txt
    while 1:
        #KMP search는 중간에 있는지 check
        #len(fix)-i로 최대 길이부터 check
        lps = post_pre(fix)
        fix = fix[:lps[len(fix)]] #txt의 길이에 해당하는 lps가 최장 pre,postfix
        
        if(KMPsearch(fix,txt)):
            print(fix)
            return

kameleon(sys.stdin.readline().rstrip('\n'))