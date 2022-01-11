#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

long long product(int a, int b, int c);

int main()
{
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);

	printf("%lld", product((a%c), b, c));
}

long long product(int a, int b, int c)
{

	if (b > 1)
	{
		long long n = product(a, b / 2, c);
		long long temp = ((n * n) % c);

		if (b % 2 == 0)
			return temp;
		else
			return (temp * a) % c;
	}
	else
		return a;
}