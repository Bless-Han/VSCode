#include <stdio.h>

typedef struct 
{
    int a;
    int b;
} two_number;

int main()
{
    two_number m[2];
    m[0].a = 20;
    m[1] = m[0];
    printf("m: %i %p \nm: %i %p\n", m[0].a, &m[0], m[1].a, &m[1]);
}