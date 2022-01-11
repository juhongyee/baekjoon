#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char* chess[8];
	char tmp[9];

	int count = 0,len;

	for (int i = 0; i < 8; i++)
	{
		scanf("%s", tmp);
		len = strlen(tmp);
		chess[i] = (char*)calloc(len + 1, sizeof(char));
		strcpy(chess[i], tmp);
	}

	for (int k = 0; k < 8; k++)
	{
		if (k % 2 == 0)
		{
			for (int j = 0; j < 8; j += 2)
			{
				if (chess[k][j] == 'F')
					count++;
			}
		}
		if (k % 2 == 1)
		{
			for (int j = 1; j < 8; j += 2)
			{
				if (chess[k][j] == 'F')
					count++;
			}
		}
	}
	printf("%d", count);

	return 0;
}