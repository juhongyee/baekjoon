#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX_INT 100000
#define HEAP_EMPTY(n) (!n)

int heap[MAX_INT + 2];
int n = 0;

void push(int item)
{
	int i;

	i = ++n;
	while ((i != 1) && (item < heap[i / 2])) {
		heap[i] = heap[i / 2];
		i /= 2;
	}
	heap[i] = item;
}

int pop()
{
	int parent, child;
	int item, temp;

	if (HEAP_EMPTY(n)) {
		return 0;
	}

	else
	{
		item = heap[1];
		temp = heap[n--];
		parent = 1;
		child = 2;

		while (child <= n)
		{
			if ((child < n) && (heap[child] > heap[child + 1]))
				child++;
			if (temp <= heap[child]) break;
			heap[parent] = heap[child];
			parent = child;
			child *= 2;
		}
		heap[parent] = temp;
		return item;
	}
}

int main()
{
	int i,input;

	scanf("%d", &i);

	for (int j = 0; j < i; j++)
	{
		scanf("%d\n", &input);

		if (!input)
			printf("%d\n", pop());
		else
			push(input);
	}

	return 0;
}