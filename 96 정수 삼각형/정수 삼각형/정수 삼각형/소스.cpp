#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n;
	int** num_tri;
	int** minimum_cost;

	scanf("%d", &n);

	num_tri = (int**)malloc(sizeof(int*) * (n+1));
	minimum_cost = (int**)malloc(sizeof(int*) * (n + 1));

	for (int i = 1; i <= n; i++)
	{
		num_tri[i] = (int*)malloc(sizeof(int) * (i+1));
		minimum_cost[i] = (int*)malloc(sizeof(int) * (i + 1));
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			scanf("%d", &num_tri[i][j]);
		}
	}

	minimum_cost[1][1] = num_tri[1][1];

	if (n == 1) {
		printf("%d", minimum_cost[1][1]);
		return 0;
	}
	else
	{
		for (int i = 2; i <= n; i++)
		{
			for (int j = 1; j <= i; j++)
			{
				if (j != 1 && j != i)
					minimum_cost[i][j] = (minimum_cost[i - 1][j] > minimum_cost[i - 1][j - 1] ? minimum_cost[i - 1][j] + num_tri[i][j] : minimum_cost[i - 1][j - 1] + num_tri[i][j]);

				else if (j == 1)
					minimum_cost[i][j] = minimum_cost[i - 1][j] + num_tri[i][j];
				else
					minimum_cost[i][j] = minimum_cost[i - 1][j-1] + num_tri[i][j];
			}
		}
	}

	int max = -1;

	for (int i = 1; i <= n; i++)
	{
		if (max < minimum_cost[n][i])
			max = minimum_cost[n][i];
	}

	printf("%d", max);

}