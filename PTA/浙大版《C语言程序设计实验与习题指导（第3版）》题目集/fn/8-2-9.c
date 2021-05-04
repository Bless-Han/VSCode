#include <stdio.h>
#define MAXN 10

void f( long int x, char *p );

int main()
{
    long int x;
    char s[MAXN] = "";

    scanf("%ld", &x);
    f(x, s);
    printf("%s\n", s);

    return 0;
}

/* 你的代码将被嵌在这里 */

void f( long int x, char *p )
{
	if (x){
		int n = 0;
		char s[MAXN];
		int flag = 1;
		if (x < 0) {
			flag = -1;
			x *= -1;
		}
		int tempNumber;
		char tempChar;
		while (x) {
			tempNumber = x % 16;
			if (tempNumber >= 10){
				tempChar = tempNumber - 10 + 'A';
			} else {
				tempChar = tempNumber + '0';
			}
			s[n++] = tempChar;
			x /= 16;
		}
		if (flag == 1){
			p[n] = s[n] = '\0';
			for (int i = 0; i < n; i++) {
				p[i] = s[n - i - 1];
			}
		} else {
			p[n + 1] = s[n] = '\0';
			p[0] = '-';
			for (int i = 0; i < n; i++) {
				p[i + 1] = s[n - i - 1];
			}
		}
	} else {
		p[0] = '0';
		p[1] = '\0';
	}
}
