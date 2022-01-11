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

	int tree_size = pow(2,ceil(log(n) / log(2)) + 1); //왜 이렇게 해야 하더라...? complete binary하려고 그런건데

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
	/*세그먼트 트리의 start와 end는 각 노드가 어디서부터 어디까지의 합인지를 표현*/
	if (left > end || right < start) return 0; // 애초에 포함이 안되어 있으면 구할 필요가 없음.
	if (left <= start && end <= right) return tree[node]; //합의 범위 내에 start외 end가 정확히 들어가 있다면 return
	//이 다음은 걸쳐 있는 경우. 범위를 줄이다 보면 무조건 들어가게 되어 있음. 계속 걸쳐 있을 수 없음. 계속 나뉘니까
	//각기 다른 부분을 관장하는 부분들로 나뉘어지므로 결국은 다 다른 녀석들의 합이 됨.
	int mid = (start + end) / 2;

	return sum(start, mid, node * 2, left, right, tree) + sum(mid + 1, end, node * 2 + 1, left, right, tree);
}