#include <stdio.h>
#include <string.h>

const int MAX_N = 500;
int main(void)
{
	char s[MAX_N + 1];
	int i;
	for (i = 0; (s[i] = getchar()) != '\n'; i++) ;
	s[i] = '\0';
	int flag = 1;
	int number = 0;
	int len = strlen(s);
	for (i = 0; i < len; i++) {
		if (s[i] != ' ') {
			if (flag == 1) number++;
			flag = 0;
		} else flag = 1;
	}
	printf("%d\n", number);
	return 0;
}
