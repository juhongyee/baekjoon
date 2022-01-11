#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#define max_size 10000001

void erato();

long arr[max_size];

int main()
{
	long n;
	bool fin = false;
	erato();

	scanf("%ld", &n);

	if (n == 1)
		return 0;

	while (1)
	{
		for (long i = 2; i < max_size; i++){ 
		
		if(arr[i]!=0)
			{
				if (n == arr[i])
				{
					fin = true;
					printf("%ld", arr[i]);
					break;
				}
				if (n % arr[i] == 0)
				{
					printf("%ld\n", arr[i]);
					n = n / arr[i];
					break;
				}
			}
		}
		if (fin == true)
			break;
	}
}

void erato()
{
	arr[0] = 0;
	arr[1] = 0;
	
	for (long i = 2; i < max_size ; i++)
		arr[i] = i;

	for (long i = 2; i < max_size ; i++)
	{
		if (arr[i] != 0)
		{
			for (long j = 2 * i; j < max_size; j += i)
				arr[j] = 0;
		}
	}

}