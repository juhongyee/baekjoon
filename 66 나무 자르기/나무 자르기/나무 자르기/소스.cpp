#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b)
{
	long long num1 = *(long long*)a;
	long long num2 = *(long long*)b;

	if (num1 > num2)
		return -1;
	else if (num1 < num2)
		return 1;
	else
		return 0;
}

int main()
{
	long long n, namu,sum = 0;
	long long* height,*arr;

	scanf("%lld %lld", &n, &namu);

	height = (long long*)calloc(n, sizeof(long long));
	arr = (long long*)calloc(n, sizeof(long long));

	for (int i = 0; i < n; i++)
		scanf("%lld", &height[i]);

	qsort(height, n, sizeof(long long), compare);

	arr[0] = height[0] - height[1];

	if (arr[0] >= namu)
	{
		printf("%lld", height[0] - namu);
		return 0;
	}

	for (int i = 1; i < n-1; i++)
	{
		arr[i] = arr[i - 1] + (i + 1) * (height[i] - height[i + 1]);
			//마지막 꺼 고려해야 함
		if (arr[i] == namu)
		{
			printf("%lld", height[i + 1]);
			return 0;
		}
		else if (arr[i] > namu)
		{
			for (int k = 1; k <= height[i] - height[i + 1]; k++)
				if (arr[i] - k * (i + 1) < namu)
				{
					printf("%lld", height[i+1] + k-1);
					return 0;
				}
		}

		if (i == n - 2)
		{
			arr[n - 1] = arr[n - 2] + n * height[n - 1];

			if (arr[n-1] == namu)
			{
				printf("0");
				return 0;
			}
			else if (arr[n-1] > namu)
			{
				for (int k = 1; k <= height[n-1]; k++)
					if (arr[n-1] - k * n < namu)
					{
						printf("%d",k-1);
						return 0;
					}
			}
		}
	}
}