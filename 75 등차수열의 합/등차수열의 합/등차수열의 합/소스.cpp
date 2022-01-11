#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>



int main()
{
	int left, right, k;
	scanf("%d", &left);
	scanf("%d", &right);
	scanf("%d", &k);

	if (k == 2)
	{
		if (left == 1)
			if (right == 1 || right == 2)
				printf("0");
			else
				printf("%d", right - 2);
		else if (left == 2)
			if (right > 2)
				printf("%d", right - 2);
			else
				printf("0");
		else
			printf("%d", right - left + 1);
	}
	else if (k == 3)
	{
		if (left > 3) {
			int a = left / 3;
			int b = right / 3;

			if (left % 3 == 0)
				a -= 1;
			printf("%d", b - a);
		}
		else {
			if (right > 3) {
				int b = right / 3;
				printf("%d", b - 1);
			}
			else
				printf("0");
		}
	} 
	else if (k == 4)
	{
		int a = left / 2;
		int b = right / 2;
		if (left >= 14) {
			if (left % 2 == 0)
				a -= 1;
			printf("%d", b - a);
		}
		else
		{
			if (left > 10) {
				if (right >= 14)
				{
					int a = 14 / 2 - 1;
					int b = right / 2;

					printf("%d", b - a);
				}
				else
					printf("0");
			}
			else
			{
				if (right >= 14)
				{
					int a = 14 / 2 - 1;
					int b = right / 2;

					printf("%d", b - a + 1);
				}
				else
				{
					if (right >= 10)
						printf("1");
					else
						printf("0");
				}
			}
		}
	}
	else if (k == 5) {
		int a = left / 5;
		int b = right / 5;
		if (left > 10) {
			if (left % 5 == 0)
				a -= 1;
			printf("%d", b - a);
		}
		else
			if (right > 10) {
				printf("%d", b - 2);
			}
			else
				printf("0");
	}

}