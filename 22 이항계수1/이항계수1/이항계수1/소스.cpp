#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int factorial(int n);

int main()
{
	int n, k;

	scanf("%d %d", &n, &k);

	printf("%d", factorial(n) / (factorial(n - k) * factorial(k)));

	return 0;
}

int factorial(int n)
{
	if (n == 0)
		return 1;

	else if (n == 1) return 1;

	else
		return n * factorial(n - 1);
}