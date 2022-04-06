#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <queue>
#include <stdlib.h>
using namespace std;

vector<int> graph[10];
vector<int> order;
queue<int> q;

void topologicalsort(int n,int* indegree)
{
	for (int i = 1; i <=n; i++)
	{
		if (indegree[i] == 0) {
			if (graph[i].size()) {
				order.push_back(i);
				q.push(i);
				indegree[i] = -1;
			}
			else
				order.push_back(i);
		}

		while (!q.empty())
		{
			int cur = q.front();
			q.pop();

			for (int j = 0; j < graph[cur].size(); j++)
			{
				indegree[graph[cur][j]]--;
				if (indegree[graph[cur][j]] == 0)
				{
					order.push_back(graph[cur][j]);
					q.push(graph[cur][j]);
					indegree[graph[cur][j]] = -1;
				}
			}
		}
	}
}

int main()
{
	int N, M; //N : 전체 학생 수,M : 간선 개수
	int a, b;

	scanf("%d %d", &N, &M);
	int* indegree;
	indegree = (int*)calloc(N + 1, sizeof(int));


	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &a, &b);
		graph[a].push_back(b);
		indegree[b]++;
	}


	topologicalsort(N, indegree);


	for (int i = 0; i < order.size(); i++)
	{
		printf("%d ", order[i]);
	}
	free(indegree);
}