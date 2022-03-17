A = list(input())
length = len(A)

skip = False
pipe = 0
sum = 0
for i in range(length):

    if(skip):
        A.pop
        skip = False
        continue
    else:
        temp = A.pop

        if(temp == ')'):
            if(A[length-1-i-1] == '('):
                skip=True
                sum += pipe

            else:
                pipe += 1
        else:
            sum += 1
            pipe -= 1

print(sum)    
