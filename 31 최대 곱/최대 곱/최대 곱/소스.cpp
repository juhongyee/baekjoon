#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main()
{
	int a, b, m, r;
	long long g;

	scanf("%d %d", &a, &b);

	m = a / b;
	r = a % b;
	g = pow(m, b - r) * pow(m + 1, r);

	printf("%lld",g);
}