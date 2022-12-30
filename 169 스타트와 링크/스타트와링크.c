#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
int calculate(bool* start, bool* link, int** arr,int N)
{
    int result_start = 0;
    int result_link = 0;
    for(int i = 0;i<N;i++)
    {
        if(start[i]==true) //true이면 그 뒤로 쭉 확인해서 true이면 더해줌.
        {
            for(int j=i;j<N;j++)
            {
                if(start[j]==true)
                {
                    result_start += arr[i][j];
                    result_start += arr[j][i];
                }
            }
        }
        else
        {
            for(int j=i;j<N;j++)
            {
                if(link[j]==true)
                {
                    result_link += arr[i][j];
                    result_link += arr[j][i];
                }
            }
        }
    }
    return abs(result_start-result_link);
}
int make_team(int** arr,int N)
{
    int min = pow(2,31)-1;
    bool start[N];
    bool link[N];
    int range = (int)pow(2,N);

    for(int i = 0;i<range;i++)
    {
        int num = 0;
        for(int j = 0;j<N;j++)
        {
            if((i&(1<<j))!=0)
            {
                num++;
                start[j] = true;
                link[j] = false;
            }
            else
            {
                link[j] = true;
                start[j] = false;
            }
        }

        if(num == (N/2))
        {
            int cal = calculate(start,link,arr,N);

            if(min>cal){
                min = cal;
            }
        }
    }

    return min;
}
int main()
{
    int N;
    scanf("%d",&N);
    getchar();

    int* arr[N];

    for(int i = 0;i<N;i++)
    {
        arr[i] = (int*)calloc(N,sizeof(int));
    }

    for(int i = 0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }

    printf("%d",make_team(arr,N));

    for(int i = 0;i<N;i++)
    {
        free(arr[i]);
    }
}