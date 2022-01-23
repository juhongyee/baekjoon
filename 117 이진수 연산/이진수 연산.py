#이진수로 입력받기
a = input()
b = input()
#문자열로 입력받은 이진수를 십진수로 바꿔주는 입력임

#bin을 쓰면 다시 십진수를 이진수로 바꿔줌.


#and 연산
for i in range(0,100000):
    if(a[i]=='1' and b[i] =='1'):
        print('1',end ='')
    else:
        print('0',end ='')
print('')

#or 연산
for i in range(0,100000):
    if(a[i]=='1' or b[i] =='1'):
        print('1',end ='')
    else:
        print('0',end ='')
print('')

#xor 연산
for i in range(0,100000):
    if(a[i] != b[i]):
        print('1',end ='')
    else:
        print('0',end ='')
print('')

#~연산
for i in range(0,100000):
    if(a[i]=='0'):
        print('1',end ='')
    else:
        print('0',end ='')
print('')

for i in range(0,100000):
    if(b[i]=='0'):
        print('1',end ='')
    else:
        print('0',end ='')
print('')
