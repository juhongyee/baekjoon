#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
	int wei;
	int val;
} thing;

int main()
{
	int n, k, ** val;
	thing* things;


	scanf("%d %d", &n, &k);

	things = (thing*)calloc(n+1, sizeof(thing));
	val = (int**)calloc(n+1,sizeof(int*));

	for (int i = 0; i <= n; i++)
	{
		val[i] = (int*)calloc(k+1,sizeof(int));
	}

	for (int i = 1; i <= n; i++)
	{
		scanf("%d %d", &things[i].wei, &things[i].val);
	}

	for(int i = 1;i<=n;i++)
		for (int j = 1; j <= k; j++)
		{
			int wi = things[i].wei;
			int value = things[i].val;

			if (wi > j)
				val[i][j] = val[i - 1][j];
			else
				val[i][j] = val[i - 1][j] > value + val[i - 1][j - wi] ? val[i - 1][j] : value + val[i - 1][j - wi];
		}

	printf("%d", val[n][k]);

	free(things);
}