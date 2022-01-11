#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int n, count = 0,a,b,c,d = 0;

	scanf("%d", &n);

	a = n / 10;
	b = n % 10;

	c = a + b;

	d = b * 10 + (c % 10);
	count++;

	while (n != d)
	{
		a = d / 10;
		b = d % 10;

		c = a + b;

		d = b * 10 + (c % 10);
		count++;
	}

	printf("%d", count);
}