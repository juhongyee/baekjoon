#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

#define max_size 250000

void erato(int arr[], int i);

int main()
{
	int n,arr[max_size+1];
	int count = 0;

	for (int i = 0; i < max_size; i++)
		arr[i] = 1;
	arr[0] = 0;
	arr[1] = 0;

	for(int i =2;i<=max_size;i++)
		if (arr[i] == 1) {
			for (int j = i + i; j < max_size; j += i)
				arr[j] = 0;
		}
	

	while (1)
	{
		scanf("%d", &n);
		count = 0;
		if (n == 0)
			break;
		for (int i = n+1; i <= 2 * n; i++)
		{
			if (arr[i] != 0)
				count++;
		}
		printf("%d\n", count);
		
	}
}
