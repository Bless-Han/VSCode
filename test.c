#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    srand(time(0));
    printf("%lu\n", random() % 3);
    printf("%lu\n", random() % 3);
    printf("%lu\n", random() % 3);
    printf("%lu\n", random() % 3);
    printf("%lu\n", random() % 3);
    printf("%lu\n", random() % 3);
}