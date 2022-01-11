#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int n,a,b,c,d,e;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %d %d", &a, &b, &c);

		d = c / a;
		e = c % a;

		if (e != 0)
			printf("%d\n", 100 * e + d + 1);
		else
			printf("%d\n", 100 * a + d);
	}

	return 0;
}