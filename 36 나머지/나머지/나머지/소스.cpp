#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int arr[10],count = 0;
	int rest[42] = { 0 };

	for (int i = 0; i < 10; i++)
		scanf("%d", &arr[i]);

	for (int i = 0; i < 10; i++)
	{
		rest[arr[i] % 42]++;
	}

	for (int i = 0; i < 42; i++)
		if (rest[i])
			count++;

	printf("%d", count);
}