#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    long double a, b;

    scanf("%Lf %Lf", &a, &b);

    printf("%.20Lf", a / b);
}