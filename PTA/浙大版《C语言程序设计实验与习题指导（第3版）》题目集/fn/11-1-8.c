#include <stdio.h>
#define MAXS 30

char *search(char *s, char *t);
void ReadString( char s[] ) /* 裁判提供，细节不表 */
{
	int n = -1;
	while ((s[++n] = getchar()) != '\n') ;
	s[n] = '\0';
}

int main()
{
    char s[MAXS], t[MAXS], *pos;

    ReadString(s);
    ReadString(t);
    pos = search(s, t);
    if ( pos != NULL )
        printf("%d\n", pos - s);
    else
        printf("-1\n");

    return 0;
}

/* 你的代码将被嵌在这里 */

char *search(char *s, char *t)
{
	int tN = -1;
	int sN = -1;
	char *temp;
	while (s[++sN] != '\0') ;
	while (t[++tN] != '\0') ;
	int i;
	for (i = 0; i < sN; i++) {
		if (t[0] == s[i]) {
			int j;
			temp = &s[i];
			for (j = 0; j < tN; j++) {
				if (t[j] != s[i + j])
					break;
			}
			if (j == tN)
				break;
		}
	}
	if (i < sN)
		return temp;
	return NULL;
}
