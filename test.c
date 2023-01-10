#include <stdio.h>
#include <cs50.h>


typedef struct
{
    int i;
}
item;

item items[5];
int main()
{
    int i = 9;
    item test;
    test.i = 100;
    printf("%i i, %i test.i\n", i, test.i);
}
