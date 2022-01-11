#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int coin[10];
	int n, cost,count = 0;

	scanf("%d %d", &n, &cost);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", coin + i);
	}

	for (int i = n - 1; i > -1; i--)
	{
		if (cost == 0)
			break;
		if (cost - coin[i] < 0)
			continue;
		else
		{
			while (cost - coin[i] >= 0)
			{
				cost -= coin[i];
				count++;
			}
		}
	}

	printf("%d",count);
}