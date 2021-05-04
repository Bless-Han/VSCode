#include <stdio.h>
#include <string.h>

const int MAX_N = 80;
int main(void)
{
	char s[MAX_N + 1];
	int i;
	for (i = 0; (s[i] = getchar()) != '\n'; i++) ;
	s[i] = '\0';
	int len = strlen(s);
	for (i = len - 1; i >= 0; i--) printf("%c", s[i]);
	return 0;
}
