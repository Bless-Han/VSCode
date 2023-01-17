#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main()
{
    // char *s = malloc(20 * sizeof(char));
    char s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}