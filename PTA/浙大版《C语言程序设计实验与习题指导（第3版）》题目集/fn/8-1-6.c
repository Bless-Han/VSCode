#include <stdio.h>
#define MAXS 20

void f( char *p );
void ReadString( char *s ); /* 由裁判实现，略去不表 */

int main()
{
    char s[MAXS];

    ReadString(s);
    f(s);
    printf("%s\n", s);

    return 0;
}

/* 你的代码将被嵌在这里 */
void f( char *p )
{
	int n = 0;
	while (p[n] != '\0') {
		n++;
	}
	char c;
	for (int i = 0; i < n / 2; i++) {
		c = p[i];
		p[i] = p[n - 1 - i];
		p[n - 1 - i] = c;
	}
}
void ReadString( char *s ); /* 由裁判实现，略去不表 */
