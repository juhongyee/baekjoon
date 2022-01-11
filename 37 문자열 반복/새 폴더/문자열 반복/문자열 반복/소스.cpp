#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	int a,b;

	scanf("%d", &a);

	for (int i = 0; i < a; i++)
	{
		char arr1[20] = { 0 };
		scanf("%d %s", &b, arr1);

		for (int i = 0; i < strlen(arr1); i++)
			for (int k = 0; k < b; k++)
			{
				printf("%c", arr1[i]);
			}

		printf("\n");
		
	}
}