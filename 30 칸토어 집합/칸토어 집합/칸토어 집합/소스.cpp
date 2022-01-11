#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define max 531443
int canarray[max] = { 0 };

void cantor(int start,int end);

int main()
{
	int n;
	while (scanf("%d",&n) != -1)
	{
		int end = pow(3, n);
		cantor(1, end);

		for (int i = 1; i <= end; i++)
		{
			if (canarray[i] == 1) {
				printf("-");
				canarray[i] = 0;
			}
			else
				printf(" ");
		}
		printf("\n");
	}
	return 0;
}

void cantor(int start, int end)
{
	if (start == end)
	{
		canarray[start] = 1;
		return;
	}

	int mid3 = (end-start+1) / 3;

	cantor(start, start+mid3-1);
	cantor(start+(mid3*2), end);
}