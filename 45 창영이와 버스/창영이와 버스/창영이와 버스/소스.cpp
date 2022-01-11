#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int* arr1[100] = { 0 };
	int* arr2 = NULL;
	int n, m,sum = 0,input;


	scanf("%d %d", &n, &m);

	arr2 = (int*)malloc(m*sizeof(int));

	for (int i = 0; i < n; i++)
		arr1[i] = (int*)calloc(n, sizeof(int));

	for (int i = 0; i < m; i++)
	{
		scanf("%d", &input);
		arr2[i] = input;
	}

	for (int i = 0; i < n; i++)
		for (int k = 0; k < n; k++)
			scanf("%d", &arr1[i][k]);

	for (int i = 0; i < m - 1; i++)
		sum += arr1[arr2[i]-1][arr2[i+1]-1];

	printf("%d", sum);

	free(arr1);
	free(arr2);

}