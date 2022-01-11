"""
한수 출력 프로그램

Author    : 이주홍
Details   : 한 MBTI를 입력하였을 때 정반대의 MBTI를 출력하는 프로그램
Input     : 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
Output    : 자연수 N보다 작거나 같은 한수의 개수
Usage     : 한수 출력 프로그램.py
History   : 2021년 01월 27일
"""

def hansuhansu(han) :
    hanslist = list()
    for ex in range(101,han+1,1) :
        s1 = ex//100
        s2 = ex//10 - s1*10
        s3 = ex - s1*100 - s2*10
        
        if s1 + s3 == 2*s2 :
            hanslist.append(ex)

    return hanslist
    
def hansu(han) :

    if han <= 99 :

        print(han)

    if han>=100 and han<1000 :
        print(len(hansuhansu(han)) + 99)

    if han == 1000 :

        print(144)
        
        
han = int(input(""))
hansu(han)
