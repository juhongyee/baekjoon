#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    long long a;
    long long sum = 0;
    scanf("%lld", &a);

    for (int i = 1; i < a; i++)
    {
        sum += (i * a + i);
    }

    printf("%lld", sum);
}