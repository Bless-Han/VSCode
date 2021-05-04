#include <stdio.h>
#define MAXN 20

void delchar( char *str, char c );
void ReadString( char s[] ); /* 由裁判实现，略去不表 */

int main()
{
    char str[MAXN], c;

    scanf("%c\n", &c);
    ReadString(str);
    delchar(str, c);
    printf("%s\n", str);

    return 0;
}

/* 你的代码将被嵌在这里 */

void delchar( char *str, char c )
{
	int n = 0;
	while (str[n] != '\0') n++;
	int str2[n];

	int n2 = 0;
	for (int i = 0; i < n; i++) {
		if (str[i] == c)
			continue;
		str2[n2] = str[i];
		n2 ++;
	}
	str2[n2] = '\0';
	for (int i = 0; i <= n2; i++) {
		str[i] = str2[i];
	}
}
