#include <stdio.h>

typedef struct 
{
    int a;
    int b;
} two_number;

int main()
{
    two_number m;
    m.a = 20;
    m.b = 90;
    printf("m.a: %i, m.b: %i\n", m.a, m.b);
    two_number n = m;
    printf("n.a: %i, n.b: %i\n", n.a, n.b);
    printf("M address: %p, N address: %p, m, n");
}