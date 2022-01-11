#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define max_dis 200001
#define max_ver 20001
#define max_edge 300001
#define pq_empty(n) (!n)
typedef struct node* nodePointer;

typedef struct node
{
	int num;
	int cost;
	nodePointer link;
};

nodePointer createNode(int num, int cost);
void list_insertion(int u, nodePointer temp);
void shortest_path(int start,int num_ver);
void push(node item);
node pop();

int distance[max_ver];
nodePointer adjLists[max_ver];
node pq[max_edge];
int n = 0;

int main()
{
	int num_ver;
	int num_edge;
	int start;
	//nodePointer* adjLists;

	scanf("%d %d", &num_ver, &num_edge);
	scanf("%d", &start);


	for (int i = 0; i <= num_ver; i++) {
		distance[i] = max_dis;
	}//distance 초기화

	for (int i = 1; i <= num_ver; i++)
	{
		adjLists[i] = (nodePointer)malloc(sizeof(node));
		adjLists[i]->num = i;
		adjLists[i]->cost = 0;
		adjLists[i]->link = NULL;
	}//adjLists 초기화

	for (int i = 0; i < max_edge; i++)
	{
		pq[i].cost = -1*max_dis;
	}//pq 초기화

	for (int i = 0; i < num_edge; i++)
	{
		int u, v, w;
		scanf("%d %d %d", &u, &v, &w);
		nodePointer temp = createNode(v, w);
		list_insertion(u, temp);
	}

	shortest_path(start,num_ver);

	for (int i = 1; i <= num_ver; i++)
	{
		if (distance[i] == max_dis)
			printf("INF\n");
		else
			printf("%d\n", distance[i]);
	}

	for (int i = 1; i <= num_ver; i++)
		free(adjLists[i]);

}

nodePointer createNode(int num, int cost)
{
	nodePointer temp;
	temp = (nodePointer)malloc(sizeof(node));
	temp->num = num;
	temp->cost = cost;
	temp->link = NULL;

	return temp;
}

void list_insertion(int u, nodePointer temp)
{
	for (nodePointer w = adjLists[u]; w; w = w->link)
	{
		/*if(w->num == temp->num)
		{
			if (w->cost > temp->cost)
				w->cost = temp->cost;
			return;
		}*/
	}
	temp->link = adjLists[u];
	adjLists[u] = temp;
}

void shortest_path(int start,int num_ver)
{
	distance[start] = 0;
	node src;
	src.num = start;
	src.cost = 0;
	push(src);

	while (!pq_empty(n))
	{
		node temp = pop();
		int cost = -1*temp.cost;
		int place = temp.num;

		if (distance[place] < cost)
			continue;

		for (nodePointer w = adjLists[place]; w; w = w->link)
		{
			if (distance[w->num] > cost + w->cost)
			{
				distance[w->num] = cost + w->cost;
				node temp2 = (*w);
				temp2.cost = -1 * (temp2.cost+cost);
				push(temp2);
			}
		}
		
	}
	
}

void push(node item)
{
	int i = ++n;
	while ((i != 1) && (item.cost > pq[i / 2].cost))
	{
		pq[i] = pq[i / 2];
		i /= 2;
	}
	pq[i] = item;
}

node pop()
{
	int parent, child;
	node item, temp;
	
	item = pq[1];
	temp = pq[n--];
	parent = 1;
	child = 2;
	while (child <= n)
	{
		if ((child < n) && (pq[child].cost < pq[child + 1].cost))
			child++;
		if (temp.cost >= pq[child].cost) break;

		pq[parent] = pq[child];
		parent = child;
		child *= 2;
	}

	pq[parent] = temp;
	return item;
}