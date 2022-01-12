#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void bfs_1(int v,int** computer,int num_com);
short int visited[101] = { 0 };
int count = 0;

int main()
{
	int num_com; //컴퓨터의 수
	int num_edge;

	scanf("%d", &num_com);
	
	int** computer;
	computer = (int**)malloc(sizeof(int*) * (num_com+1));
	for (int i = 0; i <= num_com; i++)
	{
		computer[i] = (int*)calloc(num_com + 1,sizeof(int));
	}

	scanf("%d", &num_edge);

	for (int i = 0; i < num_edge; i++)
	{
		int first, second; //연결된 두 개의 node

		scanf("%d %d", &first, &second);
		computer[first][second] = second;
		computer[second][first] = first;
	}
	bfs_1(1,computer,num_com);
	printf("%d", count);

	for (int i = 0; i <= num_com; i++)
		free(computer[i]);
	free(computer);
}

void bfs_1(int v,int** computer,int num_com)
{
	visited[v] = true;

	for (int i = 1; i <=num_com; i++)
	{
		if (computer[v][i] != i)
			continue;
		else
		{
			if (!visited[computer[v][i]]) {
				count++;
				bfs_1(computer[v][i], computer,num_com);
			}
		}
	}

}