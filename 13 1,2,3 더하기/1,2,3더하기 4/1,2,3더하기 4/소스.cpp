#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int by(int n);

int main()
{
	int n,sum = 0,iterate;
	scanf("%d", &iterate);

	for (int k = 0; k < iterate; k++) 
	{
		sum = 0;

		scanf("%d", &n);

		for (int i = 0; i <= (n - n % 3); i += 3)
		{
			sum += by(n - i);
		}
		printf("%d\n", sum);
	}

}

int by(int n)
{
	int k;

	k = n / 2 + 1;

	return k;
}