#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ggg(int a, int b);

char product[101];

int main()
{
	int n, k;
	scanf("%d %d", &n, &k);

	ggg(n, k);

	return 0;
}

int ggg(int n, int k)
{

	char tmp[3];

	int a = 0,b=k, c;
	int temp = 0;

	if (n == 1) {
		printf("%d", k);
		return 0;
	}

	else if (k < n) {
		printf("0");
		return 0;
	}
	
	else
	{
		for (int i = 0; i < 82; i++)
		{
			sprintf(tmp, "%d", b);
			
			product[i] = tmp[0];

			for (int j = 1; j <= k / n; j++)
			{
				if (((n * b + a)%10)*10+b == 10 * k + j)
				{
					int len = strlen(product);
					
					for (int t = 0; t < len; t++)
						printf("%c", product[len - 1 - t]);
					return 0;
				}
			}
			temp = b;
			b = (n * b + a) % 10;
			a = (n * temp + a) / 10;

			if (i > 81)
			{
				printf("0");
				return 0;
			}

		}
	}

}