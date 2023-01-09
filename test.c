#include <stdio.h>
#include <cs50.h>

typedef struct
{
    string name;
}
item;

item items[5];
int main()
{
    int i;
    for (i = 0; i < 5; i++)
    {
        if (i == 4)
        {
            goto kk;
        }
    }
    kk:
    printf("%i i\n", i);
}