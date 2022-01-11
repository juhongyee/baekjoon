#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	long long n, * arr, sum1 = 0,sum2 = 0;

	scanf("%lld", &n);

	arr = (long long*)calloc(n, sizeof(long long));

	for (int i = 0; i < n; i++)
		scanf("%lld", &arr[i]);

	for (int i = 1; i < n; i++)
	{
		sum1 += arr[i - 1];
		sum2 += sum1 * arr[i];
	}

	printf("%lld", sum2);
}