#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int hap(long long d);

int main()
{
	long long x, y, z =1;
	int count;
	bool a = false;
	
	scanf("%d", &count);

	for (int i = 0; i < count; i++)
	{
		scanf("%ld %ld", &x, &y);

		if ((-1 + sqrt(1 + 4 * (y - x))) - (int)((-1 + sqrt(1 + 4 * (y - x)))) == 0)
		{
			a = true;
		}

		if (a)
		{
			if (((int)((float)(- 1 + sqrt(1 + 4 * (y - x)))/2)%2) == 0)
				printf("%ld\n", 2 * hap(y - x));
			else
				printf("%ld\n", 2 * hap(y - x)+1);
		}
		else
			if (((int)((float)(-1 + sqrt(1 + 4 * (y - x))) / 2) % 2) == 0)
				printf("%ld\n", 2 * hap(y - x) + 1);
			else
				printf("%ld\n", 2 * hap(y - x) + 2);

		a = false;
	}
}

int hap(long long d)
{
	int k = 1;
	while (k * (k + 1) < d)
		k++;

	return (k-1);
}