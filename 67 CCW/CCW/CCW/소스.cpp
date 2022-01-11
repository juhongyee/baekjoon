#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct
{
	int x;
	int y;
}point;

int CCW(point a, point b, point c);

int main()
{
	point arr[3];

	for (int i = 0; i <= 2; i++)
		scanf("%d %d", &arr[i].x, &arr[i].y);

	printf("%d", CCW(arr[0], arr[1], arr[2]));
	
	return 0;
}

int CCW(point a, point b, point c)
{
	if ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) > 0)
		return 1;
	else if ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) < 0)
		return -1;
	else
		return 0;
}