#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct
{
	long long x;
	long long y;
}point;

long long CCW(point a, point b, point c);

int main()
{
	point arr[5];

	scanf("%lld %lld %lld %lld", &arr[1].x, &arr[1].y, &arr[2].x, &arr[2].y);
	scanf("%lld %lld %lld %lld", &arr[3].x, &arr[3].y, &arr[4].x, &arr[4].y);

	if ((CCW(arr[1], arr[2], arr[3]) * CCW(arr[1], arr[2], arr[4]) < 0) && (CCW(arr[3], arr[4], arr[1]) * CCW(arr[3], arr[4], arr[2]) < 0))
		printf("1");
	else
		printf("0");
}



long long CCW(point a, point b, point c)
{
	if ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) > 0)
		return 1;
	else
		return -1;
}