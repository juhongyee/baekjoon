#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	long long pinary_number[100];
	long long remember[100];

	pinary_number[1] = 1;
	remember[1] = 2;
	pinary_number[2] = 1;
	remember[2] = 3;

	int n;
	scanf("%d", &n);

	for (int i = 3; i <= 95; i++)
	{
		pinary_number[i] = remember[i - 2];
		remember[i] = remember[i - 2] + remember[i - 1];
	}

	printf("%lld", pinary_number[n]);
}

