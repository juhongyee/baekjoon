#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>


int prime(int a);

int main()
{
	int arr1[4] = { 2,3,5,7 };
	int arr[8],temp,n;

	scanf("%d", &n);

	for (int i = 0; i < 4; i++)
		for(int j = 1;j<=9; j+=2)
			for (int j = 1; j <= 9; j += 2)


}

int prime(int a)
{
	int i = 2;

	if (a == 1)
		return 0;
	else
	{
		while (1)
		{
			if (i <= sqrt(a))
			{
				if (a % i == 0)
					return 0;
			}
			else
				return a;

			i++;
		}
	}
}