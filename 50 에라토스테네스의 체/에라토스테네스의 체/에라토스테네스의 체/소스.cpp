#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

#define max_size 1000

int main()
{
	int n,k, arr[max_size + 1], count = 0;

	scanf("%d %d", &n, &k);

	for (int i = 0; i <=n; i++)
		arr[i] = 1;
	arr[0] = 0;
	arr[1] = 0;

	for(int i =2; i<=n;i++)
		if (arr[i] == 1)
		{
			for (int j = i; j <= n; j += i)
			{
				if (arr[j]==1)
				{
									count++;
				if (count == k)
				{
					printf("%d", j);
					return 0;
				}
				arr[j] = 0;
				}
			}
		}

}