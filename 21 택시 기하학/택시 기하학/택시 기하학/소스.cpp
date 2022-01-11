#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>

int main()
{
	int radius;
	scanf("%d", &radius);

	printf("%lf\n", M_PI * pow(radius, 2));
	printf("%f", 2 * pow(radius, 2));
}