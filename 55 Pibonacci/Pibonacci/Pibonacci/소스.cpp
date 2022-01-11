#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <stdlib.h>
#define MOD 1000000000000000000

long long pibonacci(int n,long long** arr);
long long pibo(int n, int k, long long** arr);

int main()
{
	int n;
	long long** arr;

	scanf("%d", &n);

	if (n >= 4)
	{
		arr = (long long**)calloc(n + 1, sizeof(long long*));

		printf("%lld", pibonacci(n, arr) % MOD);
	}
	else
		printf("1");

	return 0;
}

long long pibonacci(int n, long long** arr)
{
	arr[3] = (long long*)calloc(1, sizeof(long long));
	arr[3][0] = { 1 };

	for (int i = 4; i <= n; i++)
		arr[i] = (long long*)calloc(int(i / M_PI)+1, sizeof(long long));

	for (int i = 4; i <= n; i++)
		arr[i][int(i/M_PI)] = 1;

	for (int i = 4; i <= n; i++)
		arr[i][0] = pibo(i, 0, arr);

	return arr[n][0]%MOD;
}

long long pibo(int n, int k, long long** arr)
{
	if (arr[n][k + 1] != 0)
	{
		return arr[n][k + 1]%MOD + arr[n - 1][k]%MOD;
	}

	else
	{
		arr[n][k+1] = pibo(n, k + 1, arr);

		return arr[n][k + 1] % MOD + arr[n - 1][k] % MOD;
	}
}