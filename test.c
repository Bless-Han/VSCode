#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main()
{
    char *s = "200";
    printf("s: %i\n", atoi(s));
}