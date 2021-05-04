#include <stdio.h>
#define N 80

char change(char c)
{
	if (c >= 'A' && c <= 'Z'){
		c = 'Z' - 'A' - (c - 'A') + 'A';
	}
	return c;
}
int main(int argc, char *argv[])
{
	char c;
	char s[N + 1];
	int i = 0;
	while ((c = getchar()) != '\n'){
		c = change(c);
		s[i++] = c;
	}
	s[i] = '\0';
	printf("%s\n", s);
	return 0;
}
