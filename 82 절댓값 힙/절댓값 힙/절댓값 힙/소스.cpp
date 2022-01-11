#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX_INT 100000
#define HEAP_EMPTY(n) (!n)
typedef struct element
{
	int key;
	short int sign;
};

element heap[MAX_INT + 2];
int n = 0;

void push(element item)
{
	int i;

	i = ++n;
	while ((i != 1) && (item.key <= heap[i / 2].key)) {
		if (item.key < heap[i / 2].key) {
			heap[i].key = heap[i / 2].key;
			heap[i].sign = heap[i / 2].sign;
			i /= 2;
		}
		else
		{
			if (item.sign > heap[i / 2].sign)
			{
				heap[i].key = heap[i / 2].key;
				heap[i].sign = heap[i / 2].sign;
				i /= 2;
			}
			else
				break;
		}
	}
	heap[i] = item;
}

element pop()
{
	int parent, child;
	element item, temp;

	if (HEAP_EMPTY(n)) {
		return { 0,0 };
	}

	else
	{
		item.key = heap[1].key;
		item.sign = heap[1].sign;
		temp.key = heap[n].key;
		temp.sign = heap[n].sign;
		n--;
		parent = 1;
		child = 2;

		while (child <= n)
		{
			if ((child < n) && (heap[child].key >= heap[child + 1].key))
				if (heap[child].key > heap[child + 1].key)
					child++;
				else
					if (heap[child].sign < heap[child + 1].sign)
						child++;
			if (temp.key <= heap[child].key)
			{
				if (temp.key < heap[child].key)
					break;
				else
					if (temp.sign > heap[child].sign)
						break;
			}
			heap[parent].key = heap[child].key;
			heap[parent].sign = heap[child].sign;
			parent = child;
			child *= 2;
		}
		heap[parent] = temp;
		return item;
	}
}

int main()
{
	int i, input;
	scanf("%d", &i);

	for (int j = 0; j < i; j++)
	{
		element ele_heap;
		scanf("%d", &input);

		if (!input)
		{
			ele_heap = pop();
			
			if (ele_heap.sign == 0)
				printf("%d\n", ele_heap.key);
			else
				printf("%d\n", -1 * ele_heap.key);

		}
		else
		{
			if (input >= 0) {
				ele_heap.key = input;
				ele_heap.sign = 0;
				push(ele_heap);
			}
			else {
				ele_heap.key = -1*input;
				ele_heap.sign = 1;
				push(ele_heap);
			}
		}
	}

	return 0;
}
