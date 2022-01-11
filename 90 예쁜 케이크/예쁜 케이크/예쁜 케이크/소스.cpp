#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

short int cake_check(long long N);

int main()
{
	int T;
	long long N;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		scanf("%lld", &N);
		if (cake_check(N))
			printf("TAK\n");
		else
			printf("NIE\n");
	}
}

short int cake_check(long long N)
{

	if (N % 9 == 0)
		return 1;
	else if (N % 3 == 2)
		return 1;
	else
		return 0;
}