#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct node* queuePointer;
typedef struct node* nodePointer;
typedef struct node {
	int vertex;
	nodePointer link;
};
queuePointer front, rear;

#define FALSE 0
#define TRUE 1
#define MAX_VERTICES 1001
#define MAX_QUEUES 10000

short int visited[MAX_VERTICES];

void insertion(nodePointer left,nodePointer temp);
nodePointer createnode(int vertex);
void dfs(int v,nodePointer* adjLists);
void graph(nodePointer* adjLists, int vertex, nodePointer temp);
void bfs(int v, nodePointer* adjLists);
void addq(int item);
int deleteq();


int main()
{
	int N, M, V;
	int vertex1, vertex2;
	scanf("%d %d %d", &N, &M, &V);

	nodePointer* adjLists = (nodePointer*)malloc((N + 1) * sizeof(nodePointer));

	for (int i = 0; i < N + 1; i++) {
		adjLists[i] = (nodePointer)malloc(sizeof(node));
		adjLists[i]->link = NULL;
	}

	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &vertex1, &vertex2);
		nodePointer temp = createnode(vertex2);
		nodePointer temp2 = createnode(vertex1);
		graph(adjLists, vertex1, temp);
		graph(adjLists, vertex2, temp2);
	}

	dfs(V, adjLists);

	for (int i = 0; i < MAX_VERTICES; i++)
		visited[i] = FALSE; //clear

	printf("\n");

	bfs(V, adjLists);


	free(adjLists);
}

nodePointer createnode(int vert)
{
	nodePointer temp;
	temp = (nodePointer)malloc(sizeof(node));
	temp->vertex = vert;
	temp->link = NULL;

	return temp;
}

void dfs(int v,nodePointer* adjLists)
{
	nodePointer w;
	visited[v] = TRUE;
	printf("%d ", v);
	for (w = adjLists[v]->link; w; w = w->link)
	{
		if (!visited[w->vertex])
			dfs(w->vertex,adjLists);
	}

}

void insertion(nodePointer left,nodePointer temp)
{
	temp->link = left->link;
	left->link = temp;
}

void graph(nodePointer* adjLists, int vertex, nodePointer temp)
{
	for (nodePointer w = adjLists[vertex]; w; w = w->link)
	{
		if (w->link == NULL) {
			w->link = temp;
			break;
		}
		if (temp->vertex < (w->link)->vertex)
		{
			insertion(w, temp);
			break;
		}
	}
}

void addq(int item)
{
	queuePointer temp;
	temp = (queuePointer)malloc(sizeof(node));
	temp->vertex = item;
	temp->link = NULL;
	
	if (front)
		rear->link = temp;
	else
		front = temp;
	rear = temp;
}

int deleteq()
{
	queuePointer temp = front;
	int item;
	
	item = temp->vertex;
	front = temp->link;
	free(temp);
	return item;
}

void bfs(int v, nodePointer* adjLists)
{
	nodePointer w;
	front = rear = NULL;
	printf("%d ", v);
	visited[v] = TRUE;
	addq(v);
	while (front)
	{
		v = deleteq();
		for(w = adjLists[v]->link;w;w=w->link)
			if (!visited[w->vertex])
			{
				printf("%d ", w->vertex);
				addq(w->vertex);
				visited[w->vertex] = TRUE;
			}
	}
}