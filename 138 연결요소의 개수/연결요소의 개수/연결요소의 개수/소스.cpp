#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>

using namespace std;

queue<int> q;
bool visited[1001];
vector<int>graph[1001];

void bfs(int start)
{
	q.push(start);
	visited[start] = true;

	while (!q.empty())
	{
		int current = q.front();
		q.pop();

		for (int i = 0; i < graph[current].size(); i++)
		{
			if (visited[graph[current][i]] == false) {
				q.push(graph[current][i]);
				visited[graph[current][i]] = true;
			}

		}

	}
}

int main()
{
	int n, k;
	scanf("%d %d",&n,&k);
	int count = 0;
	short int* memory;
	memory = (short int*)calloc((n+1),sizeof(short int));

	for (int i = 0; i < k; i++)
	{
		int node1;
		int node2;

		scanf("%d %d", &node1, &node2);
		memory[node1] = 1;
		memory[node2] = 1;

		graph[node1].push_back(node2);
		graph[node2].push_back(node1);
	}
	
	for (int i = 1; i < 1001; i++)
	{
		for (int j = 0; j < graph[i].size(); j++)
		{
			if (visited[graph[i][j]] == false)
			{
				bfs(graph[i][j]);
				count++;
			}
		}
	}
	for (int i = 1; i <= n; i++)
	{
		if (memory[i] == 0)
			count++;
	}
	printf("%d", count);
}