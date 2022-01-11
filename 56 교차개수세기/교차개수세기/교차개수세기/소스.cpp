#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
	int num;
	int place;
}line;

int compare(const void* a, const void* b)    // 오름차순 비교 함수 구현
{
	line num1 = *(line*)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
	line num2 = *(line*)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

	if (num1.num < num2.num)    // a가 b보다 작을 때는
		return -1;      // -1 반환

	if (num1.num > num2.num)    // a가 b보다 클 때는
		return 1;       // 1 반환

	return 0;    // a와 b가 같을 때는 0 반환
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