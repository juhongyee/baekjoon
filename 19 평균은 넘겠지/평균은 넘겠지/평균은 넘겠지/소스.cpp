#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int test, num,sum = 0,count = 0,mean;
	int arr[1000];

	scanf("%d", &test);

	for (int i = 0; i < test; i++)
	{
		count = 0;
		sum = 0;
		scanf("%d", &num);

		for (int k = 0; k < num; k++)
		{
			scanf("%d", &arr[k]);
			sum += arr[k];
		}
		mean = sum / num;

		for (int j = 0; j < num; j++)
		{
			if (arr[j] > mean)
				count++;
		}

		printf("%.3f%%\n", ((float)count / num)*100);
	}
}