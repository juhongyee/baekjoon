#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

long prime_number(long a);

int main()
{
	long start, fin, buf;
	char number[10], buffer[10];
	int len = 0, len2 = 0;
	bool finish = false;
	scanf("%ld %ld", &start, &fin);

	for (long i = start; i <= fin; i++)
	{
		if (i == 10000000)
			break;
		if (i % 2 == 0)
			continue;
		finish = false;
		len = sprintf(buffer, "%ld", i);

		strcpy(number, buffer);

		for (int k = 0; k <= len / 2 - 1; k++)
		{
			if (number[k] != number[len - 1 - k])
			{
				finish = true;
				break;
			}
		}
		if (finish)
			continue;
		buf = prime_number(i);
		if (buf)
			printf("%ld\n", buf);

	}
	printf("-1");
}

long prime_number(long a)
{
	int i;
	i = 2;

	while (1) { //무한루프 
		if (i <= sqrt(a)) {
			if (a % i == 0) { //i가 나누어떨어지면 소수가 아님 
				return 0;
			}
			else {
				i++;
			}
		}
		else { //i가 j보다 커질때까지 나누어떨어지지 않으면 소수 
			return a;
		}
	}
}