#include <stdio.h>
#define MAXN 20

void strmcpy( char *t, int m, char *s );
void ReadString( char s[] ); /* 由裁判实现，略去不表 */

int main()
{
    char t[MAXN], s[MAXN];
    int m;

    scanf("%d\n", &m);
    ReadString(t);
    strmcpy( t, m, s );
    printf("%s\n", s);

    return 0;
}

/* 你的代码将被嵌在这里 */

void strmcpy( char *t, int m, char *s )
{
	int n = 0;
	while (t[n] != '\0') n++;
	if (m > n) s[0] = '\0';
	else {
		int i;
		for (i = 0; i < n - m + 1; i++) {
			s[i] = t[i + m - 1];
		}
		s[i] = '\0';
	}
}
