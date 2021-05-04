#include <stdio.h>
#include <string.h>

#define MAXS 80

int getindex( char *s );

int main()
{
    int n;
    char s[MAXS];

    scanf("%s", s);
    n = getindex(s);
    if ( n==-1 ) printf("wrong input!\n");
    else printf("%d\n", n);

    return 0;
}

/* 你的代码将被嵌在这里 */
int getindex( char *s )
{
	if (!strcmp("Sunday", s)) return 0;
	else if (!strcmp("Monday", s)) return 1;
	else if (!strcmp("Tuesday", s)) return 2;
	else if (!strcmp("Wednesday", s)) return 3;
	else if (!strcmp("Thursday", s)) return 4;
	else if (!strcmp("Friday", s)) return 5;
	else if (!strcmp("Saturday", s)) return 6;
	return -1;
}
