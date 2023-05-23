import sys
N = int(input())

name = {'D' : 0, 'P' : 1}

X = 0
Y = 0
winner = []
for i in range(N):
    winner.append(sys.stdin.readline().strip())
for i in range(N):
    this_win = winner[i]
    if(name[this_win]):
        Y += 1
    else:
        X += 1
        
    if(i == N-1):
        print("{}:{}".format(X,Y))
        break
    elif(abs(X-Y)==2):
        print("{}:{}".format(X,Y))
        break