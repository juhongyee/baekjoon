#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

long long comb[1001][1001] = { 0 };

long long combination(int a, int b)
{
	if (a == b || b == 0)
		return 1;
	if (a - b == 1 || b == 1)
		return a;
	if (comb[a][b] != 0)
		return comb[a][b];
	else
		return comb[a][b] = combination(a - 1, b - 1) + combination(a - 1, b);
}

int main(void)
{
	int n, k;
	scanf("%d %d", &n, &k);
	printf("%lld", combination(n, k));
}