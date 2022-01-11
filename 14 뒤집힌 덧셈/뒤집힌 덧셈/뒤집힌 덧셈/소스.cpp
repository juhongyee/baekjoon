#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int REV(char* arr);

int main()
{
	char* num1,*num2,*num3;
	int num;

	num1 = (char*)malloc(5 * sizeof(char));
	num2 = (char*)malloc(5 * sizeof(char));
	num3 = (char*)malloc(5 * sizeof(char));
	
	scanf("%s %s", num1, num2);

	num = REV(num1) + REV(num2);

	sprintf(num3, "%d", num);

	printf("%d", REV(num3));
}

int REV(char* arr)
{
	char temp;
	if (strlen(arr) == 4)
	{
		temp = arr[3];
		arr[3] = arr[0];
		arr[0] = temp;
		temp = arr[2];
		arr[2] = arr[1];
		arr[1] = temp;

		return(((int)arr[0]-48) * 1000 + ((int)arr[1] - 48) * 100 + ((int)arr[2] - 48) * 10 + ((int)arr[3] - 48));
	}

	else if (strlen(arr) == 3)
	{
		temp = arr[2];
		arr[2] = arr[0];
		arr[0] = temp;
		return(((int)arr[0] - 48) * 100 + ((int)arr[1] - 48) * 10 + ((int)arr[2] - 48));
	}

	else if (strlen(arr) == 2)
	{
		temp = arr[1];
		arr[1] = arr[0];
		arr[0] = temp;

		return(((int)arr[0] - 48) * 10 + ((int)arr[1] - 48));
	}

	else
		return(((int)arr[0] - 48));
}