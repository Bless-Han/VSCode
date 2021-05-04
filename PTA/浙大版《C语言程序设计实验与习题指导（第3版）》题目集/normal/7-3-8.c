#include <stdio.h>
#define N 80

int count(char *s, char c)
{
	int ret = 0;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == c)
			ret++;
	}
	return ret;
}
int main(int argc, char *argv[])
{
	char c;
	char s[N + 1];
	int n = 0;
	while ((c = getchar()) != '\n')
		s[n++] = c;
	s[n] = '\0';
	scanf("%c\n", &c);
	printf("%d\n", count(s, c));
	return 0;
}
