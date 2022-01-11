#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

#define MAX_STACK_SIZE 100000
long long stack[MAX_STACK_SIZE];

int top = -1;
int silsu = 0;
void push(int data);
long long pop();
long long prime_number(long long a);
int mersenne(int j);

long long prime_number(long long a)
{
	int i;
	i = 2;

	while (1) { //���ѷ��� 
		if (i <= sqrt(a)) {
			if (a % i == 0) { //i�� ����������� �Ҽ��� �ƴ� 
				return i;
			}
			else {
				i++;
			}
		}
		else { //i�� j���� Ŀ�������� ����������� ������ �Ҽ� 
			return a;
		}
	}
}

int mersenne(int j)
{
	long long num = powl(2, j);
	num--;
	while (1)
	{
		long long temp = prime_number(num);

		if (temp == num && top == -1)
			return 0;
		else if (temp == num)
		{
			push(temp);
			return 1;
		}
		else
		{
			push(temp);
			num = num / temp;
		}
	}
}

void push(int data)
{
	stack[++top] = data;
}

long long pop()
{
	top--;
	return stack[silsu++];
}

int main()
{
	mersenne(59);
	while (!(top == -1))
	{
		printf("%lld", pop());
		if (!(top == -1))
			printf(" * ");
		if (top == -1) {
			long long k = powl(2, 61);
			k--;
			printf(" = %0.f = (2 ^ %d)-1", powl(2, 59) - 1, 59); printf("\n");
			silsu = 0;
		}
	}
}