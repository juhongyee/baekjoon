#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

short int visited[25][25] = { 0 };
int n;//���μ���
char** apart;//�������� ����

int x[4] = { 0,1,0,-1 };//01 10 0-1 -10
int y[4] = { 1,0,-1,0 };
int dfs(int i,int j,int count);
void print_result(int* dan);
int compare(const void* a, const void* b)    // �������� �� �Լ� ����
{
	int num1 = *(int*)a;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������
	int num2 = *(int*)b;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������

	if (num1 > num2)    // a�� b���� Ŭ ����
		return -1;      // -1 ��ȯ

	if (num1 < num2)    // a�� b���� ���� ����
		return 1;       // 1 ��ȯ

	return 0;           // a�� b�� ���� ���� 0 ��ȯ
}

int main()
{
	int dan[625] = { 0 };//�������� ����
	scanf("%d", &n);//���� ����

	apart = (char**)malloc(sizeof(char*)*n);

	for (int i = 0; i < n; i++)
		apart[i] = (char*)calloc(n, sizeof(char));

	for (int i = 0; i < n; i++)
		scanf("%s", apart[i]);

	//bfs�� ��� ����� ���� ����.
	for(int i=0;i<n;i++)
		for (int j = 0; j < n; j++)
		{
			if (apart[i][j] == '1'&&visited[i][j]!=1) {//�׳� ���°� �ƴ϶� ���밡 �����ϰ� ���� �湮���� �ʾ��� ��� bfs
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
	int k = 0;//�� ���� ����
	while (1)
	{
		if (dan[k] == 0)
		{
			break;
		}
		k++;
	}

	qsort(dan, k, sizeof(int), compare);//�� �����ͷ� �༭ �迭ũ�Ⱑ ����� �ȵ�.
	printf("%d\n", k);
	for (int i = k-1; i>-1; i--)
	{
		printf("%d\n", dan[i]);
	}
}
