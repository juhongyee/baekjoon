#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char arr1[10001], arr2[10001];
	int i = 0, k = 0;
	long sum = 0;

	scanf("%s %s", arr1, arr2);

	while (arr1[i] != '\0')
	{
		while (arr2[k] != '\0')
		{
			sum += ((int)arr1[i]-48) * ((int)arr2[k]-48);
			k++;
		}
		i++;
		k = 0;
	}

	printf("%ld", sum);

}