#include <stdio.h>

#define MAXS 10

char *match( char *s, char ch1, char ch2 );

int main()
{
    char str[MAXS], ch_start, ch_end, *p;

    scanf("%s\n", str);
    scanf("%c %c", &ch_start, &ch_end);
    p = match(str, ch_start, ch_end);
    printf("%s\n", p);

    return 0;
}

/* 你的代码将被嵌在这里 */

char *match( char *s, char ch1, char ch2 )
{
	char *ret = "";
	int n = 0;
	int flag = 0;
	while (s[n] != '\0'){
		if (s[n] == ch1 && flag == 0){
			ret = &s[n];
			printf("%c", s[n]);
			flag++;
		} else if (flag > 0){
			printf("%c",s[n]);
			if (s[n] == ch2)
				break;
		}
		n++;
	}
	printf("\n");

	return ret;
}
