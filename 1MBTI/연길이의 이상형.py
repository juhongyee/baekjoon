"""
인하대학교 프로그래밍 경진대회 1번문제

Author    : 이주홍
Details   : 한 MBTI를 입력하였을 때 정반대의 MBTI를 출력하는 프로그램
Input     : 하나의 MBTI
Output    : 입력한 MBTI와 정반대의 MBTI
Usage     : 연길이의 이상형.py
History   : 2021년 01월 14일
"""

MBTI = input("MBTI를 입력해주세요.")

MBTI1 = list(MBTI)

a = MBTI1[0]
b = MBTI1[1]
c = MBTI1[2]
d = MBTI1[3]

def convert1(a) :
    if a == 'E' :
        a = 'I'
        return a
    else :
        a = 'E'
        return a
def convert2(b) :
    if b == 'S' :
        b = 'N'
        return b
    else :
        b = 'S'
        return b
def convert3(c) :
    if c == 'T' :
        c = 'F'
        return c
    else :
        c = 'T'
        return c
def convert4(d) :
    if d == 'J' :
        d = 'P'
        return d
    else :
        d = 'J'
        return d


MBTI = convert1(a)+convert2(b)+convert3(c)+convert4(d)

print(MBTI)
