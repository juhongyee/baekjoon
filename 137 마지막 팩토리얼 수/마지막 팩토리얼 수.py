#N!의 N입력

N = int(input())
facto = 1

for i in range(1,N+1):
    facto *= i

    while(facto%10 == 0):
        facto = facto//10

    facto = facto%1000000

print(facto%10)
