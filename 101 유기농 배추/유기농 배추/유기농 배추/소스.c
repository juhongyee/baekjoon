#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int x[4] = { 0,1,0,-1 };
int y[4] = { 1,0,-1,0 };
void dfs(int i,int j,int** field, short int visited[][50]);
int width, vertical, place;

int main()
{
	int num_test; //test_case의 개수
	scanf("%d", &num_test);

	for (int k = 0; k < num_test; k++)
	{
		int** field;
		short int visited[50][50] = { 0 };
		int count = 0;

		scanf("%d %d %d", &width, &vertical, &place);

		field = (int**)malloc(sizeof(int*) * width);//가로 길이만큼 할당
		for (int i = 0; i < width; i++)
		{
			field[i] = (int*)calloc(vertical,sizeof(int));//세로 길이만큼 할당
		}
		//요소 입력
		for (int i = 0; i < place; i++)
		{
			int x1, y1;
			scanf("%d %d", &x1, &y1);

			field[x1][y1] = 1;
		}

		for (int i = 0; i < width; i++)
			for (int j = 0; j < vertical; j++)
				if (field[i][j] == 1 && !visited[i][j]) {
					count++;
					dfs(i, j, field, visited);
				}
		printf("%d\n", count);
		free(field);
	}
}

void dfs(int i,int j, int** field, short int visited[][50])
{
	int new_x, new_y;
	visited[i][j] = true;

	for (int i1 = 0; i1 < 4; i1++)
	{
		new_x = i + x[i1];
		new_y = j + y[i1];

		if(0<=new_x&& new_x <width&&new_y<vertical&&0<=new_y)
			if(field[new_x][new_y] == 1&&!visited[new_x][new_y])
				dfs(new_x, new_y, field, visited);
	}

}