"""
인하대학교 프로그래밍 경진대회 3번문제

Author    : 이주홍
Details   : 한 MBTI를 입력하였을 때 정반대의 MBTI를 출력하는 프로그램
Input     : 하나의 MBTI
Output    : 입력한 MBTI와 정반대의 MBTI
Usage     : 받아쓰기.py
History   : 2021년 01월 23일
"""

a = input("")
ss1 = input("")
ss2 = input("")
ss3 = list(ss2)
ss3.reverse()
ss4 = list(ss1)
ss4.reverse()
cm1 = ss3[0]
print(cm1)

if cm1 == 'j' or 'l' :
    n = 0
    while 1:

        cm2 = ss4[n]
        
        if cm1 == cm2 :
            break

        elif cm2 == 'i' :
            break

        n = n+1

elif cm1 == 'w' :
    n = 0
    while 1:

        cm2 = ss4[n]
        
        if cm1 == cm2 :
            break

        elif cm2 == 'v' :
            break

        n = n+1
        
else :
    n = 0
    while 1:

        cm2 = ss4[n]
        
        if cm1 == cm2 :
            print(cm2)
            break
        
        n = n+1
