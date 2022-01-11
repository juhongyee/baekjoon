#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long factorial(int n);
long long modInv(long long a, int M);

int main()
{
	int n, k;
	long a, b, c;

	scanf("%d %d", &n, &k);

	a = factorial(n);
	b = (factorial(n-k) * factorial(k))%10007;
	c = ((a * modInv(b, 10005)) % 10007);

	printf("%ld", c);

	return 0;
}

long factorial(int n)
{
	if (n == 0)
		return 1;

	else if (n == 1) return 1;

	else
		return (n * factorial(n - 1)%10007);
}

long long modInv(long long a, int M) {
	if (M == 1)
		return a;
	if (M == 0)
		return 1;

	long long  tmp = modInv(a, M / 2);
	if (M % 2)
		return (long long)((long long)((tmp * tmp) % 10007) * a) % 10007;
	else
		return (long long)(tmp * tmp) % 10007;
}