#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define mod 1000000007

long long init(int start, int end, int node, long long* tree, long long* a);
long long sum(int start, int end, int node, int left, int right, long long* tree);
long long update(int start, int end, int node, int index,long long* tree);
long long modInv(long long a, int M);

long long c;
int main()
{
	int N, M, K;
	long long* numarr;
	long long* tree;

	scanf("%d %d %d", &N, &M, &K);

	int tree_size = 4 * N;

	numarr = (long long*)malloc(sizeof(long long) * N);
	tree = (long long*)malloc(sizeof(long long) * tree_size);

	for (int i = 0; i < N; i++)
		scanf("%lld", numarr + i);

	init(0, N - 1, 1, tree, numarr);

	int a, b;

	for (int i = 0; i < M + K; i++)
	{
		scanf("%d %d %lld", &a, &b, &c);

		switch (a)
		{
		case 1:
		{
			update(0, N - 1, 1, b - 1,tree);
			numarr[b - 1] = c;

			break;
		}
		case 2:
		{
			printf("%lld\n", sum(0, N - 1, 1, b - 1, c - 1, tree));
			break;
		}
		}

	}
	free(numarr);
	free(tree);
}

long long init(int start, int end, int node, long long* tree, long long* a)
{
	if (start == end) return tree[node] = a[start]%mod;
	int mid = (start + end) / 2;

	return tree[node] = (init(start, mid, node * 2, tree, a)*init(mid + 1, end, node * 2 + 1, tree, a))%mod;
}

long long update(int start, int end, int node, int index, long long* tree)
{
	if (index<start || index>end) return tree[node]; //index가 범위 안에 없는 경우

	if (start == end) 
		return tree[node] = c; //leaf에 다다르면 그만
	int mid = (start + end) / 2;

	return tree[node] = (update(start, mid, node * 2, index,tree)*update(mid + 1, end, node * 2 + 1, index, tree))%mod; //자식 node부터 업데이트
}//왜 부모부터 갱신하면 답이 틀렸을까??? 고민을 좀 해보자. 정말

long long sum(int start, int end, int node, int left, int right, long long* tree)
{
	if (left > end || right < start) return 1;
	if (left <= start && end <= right) return tree[node]%mod;
	int mid = (start + end) / 2;

	return (sum(start, mid, node * 2, left, right, tree) * sum(mid + 1, end, node * 2 + 1, left, right, tree))%mod;
}

long long modInv(long long a, int M) {
	if (M == 1)
		return a;
	if (M == 0)
		return 1;

	long long  tmp = modInv(a, M / 2);
	if (M % 2)
		return (long long)((long long)((tmp * tmp) % mod) * a) % mod;
	else
		return (long long)(tmp * tmp) % mod;
}