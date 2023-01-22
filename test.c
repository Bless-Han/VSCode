#include <stdio.h>

typedef struct 
{
    int a;
    int b;
} two_number;

int main()
{
    char s[20];
    for (int i = 0; i < 20; i++)
    {
        /* code */
        sprintf(s, "%03i", i);
        s[2] = '\0';
        printf("s: %s\n", s);
    }
}