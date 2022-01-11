#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int n;
	long long pi = 1;
	char num[100];

	scanf("%d", &n);

	for (int i = 1; i <= n; i++)
	{
		pi = (pi * i);
		char tmp[100];
		sprintf(tmp, "%lld", pi);
		strcpy(num, tmp);

		for (int k = strlen(num) - 1; k >= 0; k--)
		{
			if (num[k] == '0')
			{
				num[k] = NULL;
			}
			else
				break;
		}

		pi = atoll(num) % 10000000000000;
	}

	pi = pi % 100000;
		printf("%05lld", pi);
}