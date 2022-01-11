#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define MAX_NUM 1001
typedef struct element* elementPointer;

typedef struct element
{
	int num;
	elementPointer link;
};

elementPointer arr[MAX_NUM];
int LIS[MAX_NUM];
int stack[MAX_NUM];
int top = -1;

int max(int a, int b,int* index,int j);
void push(int a);
int pop();

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		arr[i] = (elementPointer)malloc(sizeof(element));
	}

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &(arr[i]->num));
		arr[i]->link = NULL;
	}

	for (int i = 0; i < n; i++)
	{
		LIS[i] = 1;
		int index_max = -1;
		for (int j = 0; j < i; j++)
		{
			if (arr[j]->num < arr[i]->num)
			{
				LIS[i] = max(LIS[i], LIS[j] + 1,&index_max,j);
			}
			if(index_max != -1)
				arr[i]->link = arr[index_max];
		}
	}

	int maximum = -1;
	int max_index = -1;

	for (int i = 0; i < n; i++)
	{
		if (LIS[i] > maximum) {
			maximum = LIS[i];
			max_index = i;
		}
	}

	for (elementPointer w = arr[max_index]; w; w = w->link)
	{
		push(w->num);
	}

	printf("%d\n", maximum);

	for (int i = 0; i < maximum; i++)
	{
		printf("%d", pop());
		printf(" ");
	}
}

int max(int a, int b,int*index,int j)
{
	if (a > b)
		return a;
	else {
		*index = j;
		return b;
	}
}

void push(int item)
{
	stack[++top] = item;
}

int pop()
{
	return stack[top--];
}