#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{

	while (1)
	{
		char fall[7] = { 0 };

		scanf("%s", fall);

		if (fall[0] == '0')
			break;

		for (int i = 0; i <= strlen(fall)/2; i++)
		{
			if (fall[i] != fall[strlen(fall)-1 - i])
			{
				printf("no\n");
				break;
			}

			if (i == strlen(fall) / 2)
				printf("yes\n");
		}

	}
}