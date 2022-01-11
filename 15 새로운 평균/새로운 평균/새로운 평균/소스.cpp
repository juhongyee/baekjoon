#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int mymax(int* arr,int n);


int main()
{
	int n, max;
	int* arr;
	float mean,sum = 0;
	
	scanf("%d", &n);
	
	arr = (int*)calloc(n, sizeof(int));

	for (int k = 0; k < n; k++)
	{
		scanf("%d", &arr[k]);
	}

	max = mymax(arr,n);

	for (int i = 0; i < n; i++)
	{
		sum += ((float)arr[i] / max) * 100;
	}

	mean = sum / n;
	printf("%.4f", mean);
}

int mymax(int* arr, int n)
{
	int max = arr[0];

	for (int i = 1; i < n; i++)
	{
		if (max <= arr[i])
			max = arr[i];
	}

	return max;
}