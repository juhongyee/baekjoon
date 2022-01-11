#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	long long n;

	scanf("%lld", &n);

	if (n == 1)
		printf("2");
	else
		printf("1");

	return 0;
}