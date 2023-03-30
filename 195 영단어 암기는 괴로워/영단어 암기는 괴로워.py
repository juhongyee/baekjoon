import sys
N,M = map(int,input().split())

num_word = {}

for i in range(N):
    string = sys.stdin.readline().strip()
    
    #M이하 제거
    if(len(string)<M):
        continue
    
    num_word[string] = num_word.get(string,0)+1

word_list = list(num_word.keys())
word_list.sort(key = lambda x : (-num_word[x],-len(x),x))

for i in range(len(word_list)):
    print(word_list[i])