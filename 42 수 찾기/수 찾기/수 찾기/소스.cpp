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

int compare(const void* a, const void* b)    // �������� �� �Լ� ����
{
	int num1 = *(int*)a;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������
	int num2 = *(int*)b;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������

	if (num1 < num2)    // a�� b���� ���� ����
		return -1;      // -1 ��ȯ

	if (num1 > num2)    // a�� b���� Ŭ ����
		return 1;       // 1 ��ȯ

	return 0;    // a�� b�� ���� ���� 0 ��ȯ
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