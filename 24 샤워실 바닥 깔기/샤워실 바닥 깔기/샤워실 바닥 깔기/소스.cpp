#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int num1, num2, num3;

	scanf("%d", &num1);
	scanf("%d %d", &num2, &num3);
	int arr1[4][4] = { {4,4,5,5},{4,3,3,5},{1,3,-1,2},{1,1,2,2} };
	int arr2[4][4] = { {4,4,5,5},{4,3,3,5},{1,3,2,-1},{1,1,2,2} };
	int arr3[4][4] = { {4,4,5,5},{4,3,3,5},{1,3,2,2},{1,1,2,-1} };
	int arr4[4][4] = { {4,4,5,5},{4,3,3,5},{1,3,2,2},{1,1,-1,2} };

	if (num1 == 1)
	{
		if (num2 == 2 && num3 == 2)
		{
			printf("1 -1\n1 1");
		}
		else if (num2 == 1 && num3 == 2)
		{
			printf("-1 1\n1 1");
		}
		else if (num2 == 1 && num3 == 1)
		{
			printf("1 1\n-1 1");
		}
		else if (num2 == 2 && num3 == 1)
		{
			printf("1 1\n1 -1");
		}
		else
			printf("-1");
	}

	if (num1 == 2)
	{
		if (num2 == 3 && num3 == 2)//1
		{
			for (int i = 0; i < 4; i++) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr1[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 3)
					printf("\n");
			}
		}
		else if (num2 == 4 && num3 == 2)
		{
			for (int i = 0; i < 4; i++) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr2[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 3)
					printf("\n");
			}
		}
		else if (num2 == 4 && num3 == 1)
		{
			for (int i = 0; i < 4; i++) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr3[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 3)
					printf("\n");
			}
		}
		else if (num2 == 3 && num3 == 1)
		{
			for (int i = 0; i < 4; i++) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr4[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 3)
					printf("\n");
			}
		}
			
		else if (num2 == 2 && num3 == 2)//1
			{
				for (int i = 0; i < 4; i++) {
					for (int k = 3; k >= 0; k--)
					{
						printf("%d", arr1[i][k]);
						if (k != 0)
							printf(" ");
					}
					if (i != 3)
						printf("\n");
				}
			}
		else if (num2 == 1 && num3 == 2)
			{
			for (int i = 0; i < 4; i++) {
				for (int k = 3; k >= 0; k--)
				{
					printf("%d", arr2[i][k]);
					if (k != 0)
						printf(" ");
				}
				if (i != 3)
					printf("\n");
			}
		}
		else if (num2 == 1 && num3 == 1)
		{
			for (int i = 0; i < 4; i++) {
				for (int k = 3; k >= 0; k--)
				{
					printf("%d", arr3[i][k]);
					if (k != 0)
						printf(" ");
				}
				if (i != 3)
					printf("\n");
			}
		}
		else if (num2 == 2 && num3 == 1)
			{
			for (int i = 0; i < 4; i++) {
				for (int k = 3; k >= 0; k--)
				{
					printf("%d", arr4[i][k]);
					if (k != 0)
						printf(" ");
				}
				if (i != 3)
					printf("\n");
			}
		}
		
		else if (num2 == 2 && num3 == 3)//1
			{
				for (int i = 3; i >= 0; i--) {
					for (int k = 3; k >= 0; k--)
					{
						printf("%d", arr1[i][k]);
						if (k != 0)
							printf(" ");
					}
					if (i != 0)
						printf("\n");
				}
			}
		else if (num2 == 1 && num3 == 3)
		{
			for (int i = 3; i >= 0; i--) {
				for (int k = 3; k >= 0; k--)
				{
					printf("%d", arr2[i][k]);
					if (k != 0)
						printf(" ");
				}
				if (i != 0)
					printf("\n");
			}
		}
		else if (num2 == 1 && num3 == 4)
		{
			for (int i = 3; i >= 0; i--) {
				for (int k = 3; k >= 0; k--)
				{
					printf("%d", arr3[i][k]);
					if (k != 0)
						printf(" ");
				}
				if (i != 0)
					printf("\n");
			}
			}
		else if (num2 == 2 && num3 == 4)
		{
			for (int i = 3; i >= 0; i--) {
				for (int k = 3; k >= 0; k--)
				{
					printf("%d", arr4[i][k]);
					if (k != 0)
						printf(" ");
				}
					if (i != 0)
						printf("\n");
				}
			}
		else if (num2 == 3 && num3 == 3)//1
		{
			for (int i = 3; i >= 0; i--) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr1[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 0)
					printf("\n");
			}
		}
		else if (num2 == 4 && num3 == 3)
		{
			for (int i = 3; i >= 0; i--) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr2[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 0)
					printf("\n");
			}
		}
		else if (num2 == 4 && num3 == 4)
		{
			for (int i = 3; i >= 0; i--) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr3[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 0)
					printf("\n");
			}
		}
		else if (num2 == 3 && num3 == 4)
		{
			for (int i = 3; i >= 0; i--) {
				for (int k = 0; k < 4; k++)
				{
					printf("%d", arr4[i][k]);
					if (k != 3)
						printf(" ");
				}
				if (i != 0)
					printf("\n");
			}
		}
		else printf("-1");
	}
}
	