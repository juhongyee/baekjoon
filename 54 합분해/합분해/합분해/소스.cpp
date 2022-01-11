#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MOD 1000000000

int comb[1001][1001];
long long combination(int a, int b);


int main()
{
	int n, k;
	long long sum = 0;

	scanf("%d %d", &n, &k);

	printf("%lld", combination(n + k - 1, k - 1)%MOD);
	return 0;
}

long long combination(int a, int b) {
	int result;
	if (a == b || b == 0)
		return 1;
	if (a - b == 1 || b == 1)
		return a;
	if (comb[a][b] != 0)
		return comb[a][b];
	else
		return comb[a][b] = combination(a - 1, b - 1) % MOD + combination(a - 1, b) % MOD;
}