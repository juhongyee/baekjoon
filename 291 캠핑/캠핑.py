import sys

i = 1
while(1):
    L,P,V = map(int,sys.stdin.readline().split())
    if(L==0 and P==0 and V==0):
        break
    ans = (V//P)*L
    ans += V%P if V%P<=L else L
    print("Case {}: {}".format(i,ans))
    i += 1