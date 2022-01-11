#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long sum_of_divisor(int n);

int main()
{
	int n;
	int input;
	scanf("%d", &n);

	for (long long i = 1; i <= n; i++)
	{
		scanf("%d", &input);
		printf("%lld\n", sum_of_divisor(input));
	}
}

long long sum_of_divisor(int n)
{
	long long sum = 0;
	for (long long i = 1; i <= n; i++)
	{
		sum += i * (n / i);
	}

	return sum;
}