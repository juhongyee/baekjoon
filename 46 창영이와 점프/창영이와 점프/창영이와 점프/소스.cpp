#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int maximum(int* arr2,int n);

int main()
{
	int n, k, count = 0,boa = 0,input = 0;
	int* arr1 = NULL, *arr2 = NULL;
	scanf("%d %d", &n, &k);

	arr1 = (int*)malloc(sizeof(int)*n);
	arr2 = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n - 1; i++) {
		scanf("%d", &input);
		arr1[i] = input;
	}

	for (int i = 0;i<n-1;i++)
		for (int j = i; j < n - 1; j++)
		{
			if (arr1[j] <= k)
				count++;
			else
			{
				if (boa == 0)
				{
					count++;
					boa++;
				}
				else
				{
					arr2[i] = count;
					count = 0;
					boa = 0;
					break;
				}

			}
			if (j == n - 2)
			{
				arr2[i] = count;
				count = 0;
				boa = 0;
			}
		}

	printf("%d", maximum(arr2,n));

	free(arr1);
	free(arr2);

	return 0;
}

int maximum(int* arr2, int n)
{
	int max = -1;

	for (int i = 0; i < n - 1; i++)
	{
		if (arr2[i] > max)
			max = arr2[i];
	}

	return max+1;
}