"""
분수 규칙 프로그램

Author    : 이주홍
Details   : 분수 규칙에 따라 분수를 출력하는 프로그램
Input     : 하나의 자연수
Output    : 자연수에 해당된 분수
Usage     : 분수_규칙_프로그램.py
History   : 2021년 01월 28일
"""

sue = int(input(""))

for n in range(1,10000,1) :

    t = (n**2-n+2)/2
    

    if sue - t == 0 :

        if (n+1)%2 == 0 :
            print("%d/%d" % (n,1))
            break
            
        else :
            print("%d/%d" % (1,n))
            break

    elif sue - t < 0 :

        if (n-1)%2 == 1 :
            k = sue - ((n-1)**2-(n-1)+2)/2
            
            print("%d/%d" % (n-1-k,1+k))
            break

        else :
            k = sue - ((n-1)**2-(n-1)+2)/2
            
            print("%d/%d" % (1+k,n-1-k))
            break    

    else :
        continue
