#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;

int main(int argc, char *argv[])
{
    printf("%lu\n", sizeof(node));
}