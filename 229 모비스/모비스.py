import sys

arr = sys.stdin.readline().strip()

M = False
O = False
B = False
I = False
S = False
for char in arr:
    if(char == 'M'):
        M = True
    if(char == 'O'):
        O = True
    if(char == 'B'):
        B = True
    if(char == 'I'):
        I = True
    if(char == 'S'):
        S = True

if(M and O and B and I and S):
    print("YES")
else:
    print("NO")