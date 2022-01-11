#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int cost[1001][3];
int minimum_cost[1001][3];
int min(int a, int b);

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++)
	{
		scanf("%d %d %d", &cost[i][0], &cost[i][1], &cost[i][2]);
	}

	minimum_cost[1][0] = cost[1][0];
	minimum_cost[1][1] = cost[1][1];
	minimum_cost[1][2] = cost[1][2];

	for (int i = 2; i <= n; i++)
	{
		minimum_cost[i][0] = min(minimum_cost[i - 1][1] + cost[i][0], minimum_cost[i - 1][2] + cost[i][0]);
		minimum_cost[i][1] = min(minimum_cost[i - 1][0] + cost[i][1], minimum_cost[i - 1][2] + cost[i][1]);
		minimum_cost[i][2] = min(minimum_cost[i - 1][0] + cost[i][2], minimum_cost[i - 1][1] + cost[i][2]);
	}

	int min = 10000000;

	for (int i = 0; i < 3; i++)
	{
		if (min > minimum_cost[n][i])
			min = minimum_cost[n][i];
	}

	printf("%d", min);
}

int min(int a, int b)
{
	if (a > b)
		return b;
	else
		return a;
}