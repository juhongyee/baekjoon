#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int top = -1;

int stack[100000];

void push(int a)
{
	top++;
	stack[top] = a;
}

void pop()
{
	stack[top] = 0;
	top--;
}

int main()
{
	int n,a,sum = 0;

	scanf("%d", &n);

	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &a);

		if (a != 0)
			push(a);
		else
			pop();
	}

	for (int i = 0; i <= top; i++)
		sum += stack[i];

	printf("%d", sum);

	return 0;
}