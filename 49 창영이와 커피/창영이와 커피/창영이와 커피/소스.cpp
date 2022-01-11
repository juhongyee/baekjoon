#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>



int main()
{
	int n, k, ** val;
	int* things;

	scanf("%d %d", &n, &k);

	if (k == 0)
	{
		printf("0");
		return 0;
	}

	things = (int*)calloc(n + 1, sizeof(int));
	val = (int**)calloc(n + 1, sizeof(int*));

	for (int i = 0; i <= n; i++)
		val[i] = (int*)calloc(k + 1, sizeof(int));

	for (int i = 1; i <= n; i++)
		scanf("%d", &things[i]);

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= k; j++)
		{
			int cafe = things[i];

			if (cafe > j)
				val[i][j] = val[i - 1][j];
			else
			{
				if (cafe == j)
					val[i][j] = 1;
				else if (val[i - 1][j] == 0 && val[i - 1][j - cafe] == 0)
					val[i][j] = 0;
				else if (val[i - 1][j] == 0)
					val[i][j] = 1 + val[i - 1][j - cafe];
				else if (val[i - 1][j - cafe] == 0)
					val[i][j] = val[i - 1][j];
				else
					val[i][j] = val[i - 1][j] <= 1 + val[i - 1][j - cafe] ? val[i - 1][j] : 1 + val[i - 1][j - cafe];
			}

		}

	if (val[n][k] != 0)
		printf("%d", val[n][k]);
	else
		printf("-1");

	free(things);
	free(val);

}


