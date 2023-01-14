#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

typedef int integer;

int main()
{
    char *s = get_string("s: ");
    char *t = malloc(strlen(s) + 1);
    
    for (int i = 0; i < strlen(s) + 1; i++)
    {
        t[i] = s[i];
    }
    
    printf("%p\n", s);
    printf("%p\n", t);
    printf("%s\n", s);
    printf("%s\n", t);
}