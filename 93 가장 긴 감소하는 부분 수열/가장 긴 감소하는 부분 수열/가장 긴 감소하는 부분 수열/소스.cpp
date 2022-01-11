#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_NUM 1001

int LIS[MAX_NUM];
int arr[MAX_NUM];

int max(int a, int b);

int main()
{
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", arr + i);

	for (int i = 0; i < n; i++)
	{
		LIS[i] = 1;
		for (int k = 0; k < i; k++)
		{
			if (arr[k] > arr[i])
			{
				LIS[i] = max(LIS[i], LIS[k] + 1);
			}
		}
	}

	int maximum = -1;
	for (int i = 0; i < n; i++)
	{
		if (LIS[i] > maximum)
			maximum = LIS[i];
	}

	printf("%d", maximum);
}

int max(int a, int b)
{
	if (a > b)
		return a;
	else
		return b;
}