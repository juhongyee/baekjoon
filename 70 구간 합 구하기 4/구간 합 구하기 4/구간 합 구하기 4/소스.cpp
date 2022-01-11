#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int init(int start, int end, int node, int* tree, int* a);
int sum(int start, int end, int node, int left, int right, int* tree);

int main()
{
	int n, m, i, j;
	int* numarr;
	int* tree;
	scanf("%d %d", &n, &m);

	int tree_size = pow(2,ceil(log(n) / log(2)) + 1); //�� �̷��� �ؾ� �ϴ���...? complete binary�Ϸ��� �׷��ǵ�

	numarr = (int*)malloc(n * sizeof(int));
	tree = (int*)malloc(tree_size * sizeof(int));

	for (int i = 0; i < n; i++)
		scanf("%d", numarr+i);

	init(0, n - 1, 1, tree, numarr);

	for (int f = 1; f <= m; f++)
	{
		scanf("%d %d", &i, &j);
		printf("%d\n", sum(0, n-1, 1, i-1, j-1, tree));
	}
	free(numarr);
	free(tree);
}

int init(int start, int end, int node, int* tree, int* a)
{
	if (start == end) return tree[node] = a[start];
	int mid = (start + end) / 2;

	return tree[node] = init(start, mid, node * 2, tree, a) + init(mid + 1, end, node * 2 + 1,tree,a);
}

int sum(int start, int end, int node, int left, int right, int* tree)
{
	/*���׸�Ʈ Ʈ���� start�� end�� �� ��尡 ��𼭺��� �������� �������� ǥ��*/
	if (left > end || right < start) return 0; // ���ʿ� ������ �ȵǾ� ������ ���� �ʿ䰡 ����.
	if (left <= start && end <= right) return tree[node]; //���� ���� ���� start�� end�� ��Ȯ�� �� �ִٸ� return
	//�� ������ ���� �ִ� ���. ������ ���̴� ���� ������ ���� �Ǿ� ����. ��� ���� ���� �� ����. ��� �����ϱ�
	//���� �ٸ� �κ��� �����ϴ� �κе�� ���������Ƿ� �ᱹ�� �� �ٸ� �༮���� ���� ��.
	int mid = (start + end) / 2;

	return sum(start, mid, node * 2, left, right, tree) + sum(mid + 1, end, node * 2 + 1, left, right, tree);
}