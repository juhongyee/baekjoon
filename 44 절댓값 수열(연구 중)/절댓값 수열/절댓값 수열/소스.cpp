#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int nnn_inspector(int nnn[], int count,int* place);//이 함수에서 nnn에 count1이 있는지 확인하고 있다면 그 자리를 계산된 숫자로 치환.아마 a1으로 치환해야할 듯,탐색알고리즘,

int main()
{
	long long a1, a2, tmp,arr[6];
	int count1 = 0, count2 = 0,n,a,nnn[50];
	int* place;
	printf("초깃값 2개와 질문개수 입력하세요\n");

	scanf("%lld %lld %d", &a1, &a2, &n);
	
	for (int i = 0; i < n; i++)
		scanf("%d", nnn[i]);

	printf("%lld\n%lld\n", a1, a2);

	while(1)
	{
		arr[count1%6] = a1;
		arr[(count1 + 1)%6] = a2;

		if (nnn_inspector(nnn, count1, place))
			nnn[*place] == a1;

		tmp = a2;
		a2 = llabs(a2 - a1);
		a1 = tmp;

		if ((arr[0] == arr[3]) && (arr[1] == arr[4]) && (arr[2] == arr[5]))
		{
			printf("%d\n", count1);
			break;
		}

		printf("%lld\n", a2);

		count1++;
	}

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &a);

		if (a < count1 - 4)
		{

		}
			
		else
		{
			if ((a - (count1 - 5)) % 3 == 1 || (a - (count1 - 5)) % 3 == 2)
			{
				for (int k = 0; k < 6; k++)
					if (arr[k] != 0)
					{
						printf("%lld", arr[k]);
						break;
					}
			}
			else if ((a - (count1 - 5)) % 3 == 0)
				printf("0\n");
		}
	}
}