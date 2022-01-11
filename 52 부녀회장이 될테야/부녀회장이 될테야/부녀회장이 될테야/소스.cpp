#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int val[15][15] = { 0 }, t, a, b;

	for (int i = 1; i <= 14; i++)
		val[0][i] = i;

	for (int i = 1; i <= 14; i++)
		for (int j = 1; j <= 14; j++)
			for (int k = 1; k <= j; k++)
				val[i][j] += val[i - 1][k];

	scanf("%d", &t);

	for (int i=1; i <= t; i++)
	{
		scanf("%d", &a);
		scanf("%d", &b);

		printf("%d\n", val[a][b]);

	}
}