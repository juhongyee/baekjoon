from bisect import bisect_left
import math
def Alphabet_check(word_list,num_cal):
    Alphabet_list = []
    
    for i in range(num_cal):
        for j in range(len(word_list[i])):
            if(not(word_list[i][j] in Alphabet_list)):
                Alphabet_list.append(word_list[i][j])
    
    return Alphabet_list

def num_check(Alphabet_list,A_num,word_list):
    for i in range(len(word_list)):
        word = word_list[i]
        len_word = len(word)
        
        for j in range(len_word):
            index = bisect_left(Alphabet_list,word[j])
            A_num[index] += math.pow(10,len_word-1-j)

num_cal = int(input())

word_list = []

for i in range(num_cal):
    word_list.append(list(input()))

Alphabet_list = Alphabet_check(word_list,num_cal)
Alphabet_list.sort()

A_num = [0 for i in range(len(Alphabet_list))]

num_check(Alphabet_list,A_num,word_list)

A_num.sort(reverse=1)

for i in range(len(A_num)):
    A_num[i] = (9-i)*A_num[i]

print(int(sum(A_num)))

#실패 ㅋㅋprint(int(sum(list(map(lambda x:x*(9-A_num.index(x)),A_num)))))