#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int n, k,count = 0;
	char num[10];

	scanf("%d %d", &n, &k);

	for (int i = 1; i <= n; i++)
	{
		sprintf(num, "%d", i);

		count += strlen(num);

		if (count == k) {
			printf("%c", num[strlen(num) - 1]);
			break;
		}
		else if (count > k)
		{
			count -= strlen(num);

			printf("%c", num[k - count - 1]);
			break;
		}

	}
}