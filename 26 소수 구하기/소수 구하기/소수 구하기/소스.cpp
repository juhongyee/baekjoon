#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

long prime_number(long a);

int main()
{
	long m, n;
	long buf=0;

	scanf("%ld %ld", &m, &n);

	for (long i = m; i <= n; i++)
	{
		if (i % 2 == 0)
			if (i == 2);
			else
				continue;

		buf = prime_number(i);

		if (buf)
			printf("%ld\n", i);

	}

	return 0;
}

long prime_number(long a)
{
	int i = 2;

	if (a == 1)
		return 0;//1은 소수가 아님.

	else
	{
		while (1)
		{
			if (i <= sqrt(a))
			{
				if (a % i == 0)
					return 0;
				else
					i++;
			}

			else
				return a;
		}
	}
}