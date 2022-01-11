#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
	int num;
	int place;
}line;

int compare(const void* a, const void* b)    // �������� �� �Լ� ����
{
	line num1 = *(line*)a;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������
	line num2 = *(line*)b;    // void �����͸� int �����ͷ� ��ȯ�� �� �������Ͽ� ���� ������

	if (num1.num < num2.num)    // a�� b���� ���� ����
		return -1;      // -1 ��ȯ

	if (num1.num > num2.num)    // a�� b���� Ŭ ����
		return 1;       // 1 ��ȯ

	return 0;    // a�� b�� ���� ���� 0 ��ȯ
}

int main()
{
	int n, m,count = 0,sum = 0;
	line* lines;

	int** arr;

	scanf("%d %d", &n, &m);

	lines = (line*)calloc(m, sizeof(line));
	arr = (int**)calloc(n + 1, sizeof(int*));

	for (int i = 0; i <= n; i++)
		arr[i] = (int*)calloc(n + 1, sizeof(int));

	for (int i = 0; i < m; i++)
	{
		scanf("%d %d", &lines[i].num, &lines[i].place);
	}

	qsort(lines, m, sizeof(line), compare);

	for (int i = 0; i < m; i++)
	{
		if (arr[lines[i].num - 1][lines[i].place] == 0) {
			for (int j = i + 1; j <= m; j++)
			{
				if (lines[i].num == lines[j].num)
					continue;
				else
				{
					if (lines[i].place > lines[j].place)
						count++;
				}
			}
			
			arr[lines[i].num][lines[i].place] = count;
			sum += count;
			count = 0;
		}

		else
		{
			for (int j = 0; j < m; j++)
			{
				if (arr[lines[j].num] == arr[lines[i].num])
					if (lines[j].place < lines[i - 1].place)
						count++;
			}

			arr[lines[i].num][lines[i].place] = arr[lines[i].num - 1][lines[i].place] - count;

			sum = arr[lines[i].num][lines[i].place];
			count = 0;
		}
	}

	printf("%d", sum);

	free(lines);
	free(arr);
}