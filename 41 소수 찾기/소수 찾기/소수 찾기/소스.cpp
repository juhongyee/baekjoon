#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>


int prime(int a);

int main()
{
	int n,count = 0,primenum;
	
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &primenum);
		if (prime(primenum))
			count++;
	}

	printf("%d", count);
}

int prime(int a)
{
	int i = 2;

	if (a == 1)
		return 0;
	else
	{
		while (1)
		{
			if (i <= sqrt(a))
			{
				if (a % i == 0)
					return 0;
			}
			else
				return a;

			i++;
		}
	}
}