#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int paac(float w, float h, int x, int y);

int main()
{
	float w, h;
	int x, y,position;
	scanf("%d %d %f %f", &x, &y, &w, &h);

	position = paac(w, h, x, y);

	if (position == 1)
	{
		if ((w - x) >= (h - y))
			printf("%.0f", h - y);
		else
			printf("%.0f", w - x);
	}
	if (position == 2)
	{
		if (x >= (h - y))
			printf("%.0f", h - y);
		else
			printf("%d", x);
	}
	if (position == 3)
	{
		if (x >= y)
			printf("%d", y);
		else
			printf("%d", x);
	}
	if (position == 4)
	{
		if ((w - x) >= y)
			printf("%d", y);
		else
			printf("%.0f", w - x);
	}
}

int paac(float w, float h, int x, int y)
{
	float criteria1 = w / 2, criteria2 = h / 2;

	if (criteria1 <= x && criteria2 <= y)
		return 1;
	else if (criteria1 >= x && criteria2 >= y)
		return 3;
	else if (criteria1 > x && criteria2 < y)
		return 2;
	else if (criteria1 < x && criteria2 > y)
		return 4;
}