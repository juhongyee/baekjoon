import math
from collections import deque

global maximum

from bisect import bisect_left

def Alphabet_check(word_list,num_cal):
    Alphabet_list = []
    
    for i in range(num_cal):
        for j in range(len(word_list[i])):
            if(not(word_list[i][j] in Alphabet_list)):
                Alphabet_list.append(word_list[i][j])
    
    return Alphabet_list

def convert(string,A_list,output):
    len_str = len(string)
    sumation = 0
    for i in range(len_str):
        index = bisect_left(A_list,string[i])
        sumation += output[index]*math.pow(10,len_str-i-1)
    
    return sumation
        

def calculate(A_list,output,word_list,num_cal):
    sumation = 0
    for i in range(num_cal):
        sumation += convert(word_list[i],A_list,output)
    
    return sumation
    
def dfs(perm,visited,depth,Alphabet_num,output,Alphabet_list,word_list,num_cal):
    global maximum
    if(depth == Alphabet_num):
        result = calculate(Alphabet_list,output,word_list,num_cal)
        if(maximum<result):
            maximum = result
            
    for i in range(Alphabet_num):
        if(visited[i]==False):
            visited[i] = True
            output.append(perm[i])
            dfs(perm,visited,depth+1,Alphabet_num,output,Alphabet_list,word_list,num_cal)
            output.pop()
            visited[i] = False
    
num_cal = int(input())

word_list = []

for i in range(num_cal):
    word_list.append(list(input()))

Alphabet_list = Alphabet_check(word_list,num_cal)
Alphabet_list.sort()

Alphabet_num = len(Alphabet_list)
#dfs를 위한 visited 선언
visited = [0 for i in range(Alphabet_num)]

#순열을 포함하기 위한 list 선언
perm = list(range(9-Alphabet_num+1,10))

#순열의 결과를 저장할 output
output = deque()

#maximum 
maximum = -math.inf

dfs(perm,visited,0,Alphabet_num,output,Alphabet_list,word_list,num_cal)

print(int(maximum))


