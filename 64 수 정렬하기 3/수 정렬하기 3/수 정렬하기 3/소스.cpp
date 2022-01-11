#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define max_size 10001

int main()
{
	int n,number;
	int count[max_size] = { 0 };

	scanf("%d", &n);
	

	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &number);
		count[number]++;
	}

	for (int i = 0; i < max_size; i++)
	{
		for (int j = 1; j <= count[i]; j++)
			printf("%d\n", i);
	}

	return 0;
}