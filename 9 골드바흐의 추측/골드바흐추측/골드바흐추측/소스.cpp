#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define prime_size 2000

int prime[prime_size];
int top = 2;
int mid;

void made_prime();
void made_arr(int* arr,int iterate);
int binary_search(int arr[], int target);

int main()
{
	prime[0] = 2;
	prime[1] = 3;
	made_prime();

	int iterate;
	
	int* arr;

	scanf("%d", &iterate);

	arr = (int*) calloc(iterate*2, sizeof(int));

	made_arr(arr,iterate);

	for (int k = 0; k < iterate * 2-1; k += 2)
		printf("%d %d\n", arr[k], arr[k + 1]);

	return 0;


}

void made_prime()
{
	for (int i = 4; i <= 10000; i++)
	{
		if ((i % 2) == 0)
			continue;
		else
		{
			for (int j = 3; j < i; j++)
			{
				if ((i % j) == 0)
					break;
				else
				{
					if (j == (i - 1))
					{
						prime[top] = i;
						top++;
					}
				}

			}
		}
	}
}

void made_arr(int* arr,int iterate)
{
	int input;
	int j = 0;
	for (int i = 0; i < iterate; i++)
	{
		scanf("%d", &input);

		for (int k = (input / 2); k >=2; k--)
		{
			if (binary_search(prime, input - k))
			{
				if (binary_search(prime, k))
				{
					arr[j] = k;
					arr[j + 1] = input - k;
					j += 2;

					break;
				}
			}	
			else
				continue;
		}
	}
}

int binary_search(int arr[], int target)
{
	int low = 0;
	int high = top;

	while (low <= high)
	{
		mid = (low + high) / 2;
		
		if (arr[mid] == target)
			return 1;
		else if (arr[mid] > target)
			high = mid - 1;
		else
			low = mid + 1;
	}
	return 0;
}