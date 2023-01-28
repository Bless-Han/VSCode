#include <stdio.h>

#define N 90

int main(int argc, char *argv[])
{
    FILE *file = fopen("test.txt", "r");
    if (file == NULL)
    {
        printf("ERROR\n");
        return 1;
    }
    char words[10][N];
    for (int i = 0; fgets(words[i], N, file); i++)
    {
        printf("i: %i\n", i);
    }
    for(int i = 0; i < 10; i++)
    {
        printf("i: %i, s: %s\n", i, words[i]);
    }

}