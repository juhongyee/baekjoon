#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void recursive(int a,int b);

int main()
{
	int a,b;

	scanf("%d", &a);

	b = a;

	printf("��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.\n");

	recursive(a,b);

	return 0;
}

void recursive(int a,int b)
{

	if (a == 0)
	{
		for (int i = 0; i < 4 * (b - a); i++)
			printf("_");
		printf("\"����Լ��� ������?\"\n");

		for (int i = 1; i <= 4 * b; i++)
			printf("_");
		printf("\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"\n");
		for (int i = 1; i <= 4 * b; i++)
			printf("_");
		printf("��� �亯�Ͽ���.\n");
	}

	else
	{
		for (int i = 0; i < 4 *(b-a) ; i++)
			printf("_");
		printf("\"����Լ��� ������?\"\n");
		for (int i = 0; i < 4 * (b - a); i++)
			printf("_");
		printf("\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.\n");
		for (int i = 0; i < 4 * (b - a); i++)
			printf("_");
		printf("���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.\n");

		for (int i = 0; i < 4 * (b - a); i++)
			printf("_");
		printf("���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"\n");

		recursive(a - 1,b);
		
		for (int i = 1; i <= 4 * (b - a); i++)
			printf("_");
		printf("��� �亯�Ͽ���.\n");
	}
}