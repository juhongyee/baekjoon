#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_QUEUE_SIZE 10000

int queue[MAX_QUEUE_SIZE];
int rear = -1;
int front = -1;

int empty()
{
	return (front == rear);
}

void addq(int item)
{
	queue[++rear] = item;
}

int deleteq()
{
	if (empty())
		return -1;
	
	return(queue[++front]);
}

int size()
{
	return rear - front;
}

int ffront()
{
	if (empty())
		return -1;
	return queue[front+1];
}

int back()
{
	if (empty())
		return -1;
	return queue[rear];
}

void input();

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		input();
	}

	return 0;
}

void input()
{
	char string[7];
	int x;

	scanf("%s", string);

	if (string[0] == 'p' && string[1] == 'u')
	{
		scanf(" %d", &x);
		addq(x);
	}
	else if (string[0] == 'p' && string[1] == 'o')
		printf("%d\n", deleteq());

	else if (string[0] == 's' && string[1] == 'i')
		printf("%d\n", size());

	else if (string[0] == 'e' && string[1] == 'm')
		printf("%d\n", empty());

	else if (string[0] == 'f' && string[1] == 'r')
		printf("%d\n", ffront());

	else if (string[0] == 'b' && string[1] == 'a')
		printf("%d\n", back());
}

