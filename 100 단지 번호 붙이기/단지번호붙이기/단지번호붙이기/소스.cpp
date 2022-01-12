#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

short int visited[25][25] = { 0 };
int n;//가로세로
char** apart;//세대정보 저장

int x[4] = { 0,1,0,-1 };//01 10 0-1 -10
int y[4] = { 1,0,-1,0 };
int dfs(int i,int j,int count);
void print_result(int* dan);
int compare(const void* a, const void* b)    // 내림차순 비교 함수 구현
{
	int num1 = *(int*)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
	int num2 = *(int*)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

	if (num1 > num2)    // a가 b보다 클 때는
		return -1;      // -1 반환

	if (num1 < num2)    // a가 b보다 작을 때는
		return 1;       // 1 반환

	return 0;           // a와 b가 같을 때는 0 반환
}

int main()
{
	int dan[625] = { 0 };//단지수를 저장
	scanf("%d", &n);//가로 세로

	apart = (char**)malloc(sizeof(char*)*n);

	for (int i = 0; i < n; i++)
		apart[i] = (char*)calloc(n, sizeof(char));

	for (int i = 0; i < n; i++)
		scanf("%s", apart[i]);

	//bfs를 모든 행렬을 돌며 돌림.
	for(int i=0;i<n;i++)
		for (int j = 0; j < n; j++)
		{
			if (apart[i][j] == '1'&&visited[i][j]!=1) {//그냥 도는게 아니라 세대가 존재하고 아직 방문하지 않았을 경우 bfs
				int count = 0;
				count = dfs(i, j,count);
				if (count) {
					int k = 0;
					while (1)
					{
						if (dan[k] == 0) {
							dan[k] = count;
							break;
						}
						k++;
					}
				}
			}
		}
	print_result(dan);
}

int dfs(int i, int j,int count)
{
	visited[i][j] = true;
	count++;

	for (int k = 0; k < 4; k++)
	{
		int new_x = i + x[k];
		int new_y = j + y[k];

		if (0 <= new_x && new_x < n && 0 <= new_y && new_y < n)
		{
			if (apart[new_x][new_y] == '1'&&!visited[new_x][new_y])
				count = dfs(new_x, new_y,count);
		}
	}

	return count;
}

void print_result(int* dan)
{
	int k = 0;//총 단지 개수
	while (1)
	{
		if (dan[k] == 0)
		{
			break;
		}
		k++;
	}

	qsort(dan, k, sizeof(int), compare);//아 포인터로 줘서 배열크기가 제대로 안들어감.
	printf("%d\n", k);
	for (int i = k-1; i>-1; i--)
	{
		printf("%d\n", dan[i]);
	}
}
