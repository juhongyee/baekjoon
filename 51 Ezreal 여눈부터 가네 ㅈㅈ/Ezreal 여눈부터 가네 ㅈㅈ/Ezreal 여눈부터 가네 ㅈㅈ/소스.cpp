#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MOD 1000000007

long long combination(int a,int b);
long factorial(int n);
long long modInv(long long a, long M);

int main()
{
	int n;
	long long sum = 0;

	scanf("%d", &n);

	for(int i = 0; i<n;i++)
		if (((n - 1) + 4 * i+5)%3 == 0)
		{
			sum += combination(n-1, i);
			sum %= MOD;
		}

	printf("%lld", sum);
}

long long combination(int n, int r)
{
	long long a, b, c;

	a = factorial(n);
	b = (factorial(n - r) * factorial(r)) % MOD;
	c = ((a * modInv(b, MOD-2)) % MOD);

	return c;
}

long factorial(int n)
{
	if (n == 0)
		return 1;

	else if (n == 1) return 1;

	else
		return (n * factorial(n - 1) % MOD);
}

long long modInv(long long a, long M) {
	if (M == 1)
		return a;
	if (M == 0)
		return 1;

	long long  tmp = modInv(a, M / 2);
	if (M % 2)
		return (long long)((long long)((tmp * tmp) % MOD) * a) % MOD;
	else
		return (long long)(tmp * tmp) % MOD;
}