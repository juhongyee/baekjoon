#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int n1,n2,sum = 0;
	char arr[8],arr2[8];

	scanf("%d", &n1);

	sprintf(arr, "%d", n1);

	n2 = n1 - strlen(arr) * 9;

	sprintf(arr2, "%d", n2);

	for (int i = 0; i <= n1 - n2; i++)
	{
		if (i == n1 - n2)
			printf("0");

		sprintf(arr2, "%d", n2+i);
		sum = n2 + i;

		for (int k = 0; k < strlen(arr2); k++)
			sum += (int)arr2[k] - 48;

		if (sum == n1)
		{
			printf("%d", n2 + i);
			break;
		}
	}
	return 0;
}