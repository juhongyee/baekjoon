import sys

def check(key,divide):
    for i in range(len(key)//divide-1):
        if(key[i*divide:(i+1)*divide]!=key[(i+1)*divide:(i+2)*divide]):
            return (False,None)
    return (True,key[0:divide])

make_num = {}
for i in range(65,91):
    make_num[chr(i)] = i-64

def convert(string):
    new = []
    for i in range(len(string)):
        new.append(make_num[string[i]])
    
    return new
    
arr = sys.stdin.readline().rstrip('\n')
result = sys.stdin.readline().rstrip('\n')

arr = convert(arr)
result = convert(result)

key = []

for i in range(len(arr)):
    x_1 = result[i]-arr[i]
    x_2 = result[i]+26-arr[i]
    
    if(26>=x_1>=1):
        key.append(x_1)
    else:
        key.append(x_2)

for i in range(1,len(key)+1):
    if(len(key)%i==0):
        flag = check(key,i)
        if(flag[0]):
            for i in range(len(flag[1])):
                print(chr(flag[1][i]+64),end = '')
            break