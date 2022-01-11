#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define max_size 100001

int compare(const void* a, const void* b);
int BSearch(int target, int length);

int arr1[max_size], arr2[max_size];

int main()
{
	int n,m;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", arr1 + i);

	scanf("%d", &m);

	for (int i = 0; i < m; i++)
		scanf("%d", arr2 + i);

	qsort(arr1, n, sizeof(int), compare);

	for (int i = 0; i < m; i++)
	{
		printf("%d\n", BSearch(arr2[i], n));
	}


	return 0;
}

int compare(const void* a, const void* b)    // 오름차순 비교 함수 구현
{
	int num1 = *(int*)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
	int num2 = *(int*)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

	if (num1 < num2)    // a가 b보다 작을 때는
		return -1;      // -1 반환

	if (num1 > num2)    // a가 b보다 클 때는
		return 1;       // 1 반환

	return 0;    // a와 b가 같을 때는 0 반환
}

int BSearch(int target,int length) {
	int low = 0;
	int high = length-1;
	int mid;

	while (low <= high) {
		mid = (low + high) / 2;

		if (arr1[mid] == target)
			return 1;
		else if (arr1[mid] > target)
			high = mid - 1;
		else
			low = mid + 1;
	}
	return 0;
}