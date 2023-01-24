#include <stdio.h>
#include <stdlib.h>

int main()
{
    char lk[200] = {0};
    char *s = malloc(3 * sizeof(char));
    char kk[200] = {0};
    if (s == NULL)
    {
        return 1;
    }
    s[0] = 'h';
    s[1] = 'i';
    s[2] = '!';
    
    s[3] = '!';
    s[4] = '!';
    s[5] = '!';
    s[6] = '!';
    s[7] = '!';
    s[8] = '!';
    s[9] = '!';
    s[10] = '!';
    // s[9] = '\0';
    printf("s: %lu\n", sizeof(s));
    printf("s: %s\n", s);
    free(s);
    return 0;
}