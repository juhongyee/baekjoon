#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
int prime_number(int a);
int fall(int a);

int main()
{
	int n,i=0;
	scanf("%d", &n);

	while (1)
	{
		if(fall(n+i))
			if (prime_number(n+i))
			{
				printf("%d", n+i);
				return 0;
			}

		i++;

	}

}

int fall(int a)
{
	char buf[10];

	sprintf(buf, "%d", a);

	int r = strlen(buf) / 2;

	for (int i = 0; i < r; i++)
	{
		if (buf[i] != buf[strlen(buf) -1 - i])
			return 0;
	}

	return 1;
}

int prime_number(int a)
{
	int i = 2;

	if (a == 1)
		return 0;

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