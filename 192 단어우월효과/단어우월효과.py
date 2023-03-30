import sys
word = {}

N = int(input())

for i in range(N):
    input_word1 = sys.stdin.readline().strip()
    if(len(input_word1)!=1):
        input_word2 = list(input_word1[1:len(input_word1)-1])
        input_word2.sort()
        input_word2 = list(input_word1[0])+input_word2+list(input_word1[-1])
        input_word2 = str(input_word2)
    else:
        input_word2 = input_word1
    word[input_word2] = input_word1

M = int(input())

arr = list(sys.stdin.readline().split())

for i in range(len(arr)):
    if(i!=len(arr)-1):
        string = arr[i]
        if(len(string)!=1):
            string2 = list(string[1:len(string)-1])
            string2.sort()
            string = list(string[0]) + string2 + list(string[-1])
            string = str(string)
        print(word[string],end=' ')
    else:
        string = arr[i]
        if(len(string)!=1):
            string2 = list(string[1:len(string)-1])
            string2.sort()
            string = list(string[0]) + string2 + list(string[-1])
            string = str(string)
        print(word[string])