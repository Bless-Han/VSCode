#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen("test.txt", "r");
    if (file == NULL)
    {
        printf("ERROR\n");
        return 1;
    }
    char words[10][5];
    for (int i = 0; fgets(words[i], 5, file); i++)
    {
        printf("i: %i\n", i);
    }
    for(int i = 0; i < 10; i++)
    {
        printf("i: %i, s: %s\n", i, words[i]);
    }

}