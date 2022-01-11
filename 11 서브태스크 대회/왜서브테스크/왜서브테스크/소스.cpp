#include <stdio.h>

int main()
{
    int n, k, l;
    int easy, hard, hum = 0, eum = 0;
    int sum = 0;

    scanf("%d %d %d", &n, &k, &l);

    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &easy, &hard);

        if (hard <= k)
            hum++;
        else if (easy <= k)
            eum++;
    }

    if (l >= n)
        sum = 140 * hum + 100 * eum;
    else {
        if (hum >= l)
            sum = 140 * l;
        else
        {
            if (l - hum >= eum)
                sum = 140 * hum + 100 * eum;
            else
                sum = 140 * hum + 100 * (l - hum);
        }
    }
    printf("%d", sum);

    return 0;
}