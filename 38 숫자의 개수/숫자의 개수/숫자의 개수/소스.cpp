#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int sum = 1, a;
	char tmp[11];
	int number[10] = { 0 };

	for (int i = 0; i < 3; i++)
	{
		scanf("%d", &a);
		sum *= a;
	}

	sprintf(tmp, "%d", sum);

	for (int i = 0; i < strlen(tmp); i++)
	{
		number[(int)tmp[i] - 48]++;
	}

	for (int k = 0; k < 10; k++)
		printf("%d\n", number[k]);

	return 0;
}