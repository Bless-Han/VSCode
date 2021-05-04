#include <stdio.h>
#define N 30

int main(int argc, char *argv[])
{
	char c;
	char s[N + 1];
	int n = 0;
	while ((c = getchar()) != '#'){
		if (c >= 'a' && c <= 'z')
			c = c - 'a' + 'A';
		else if (c >= 'A' && c <= 'Z')
			c = c - 'A' + 'a';
		s[n++] = c;
	}
	s[n] = '\0';
	printf("%s\n", s);
	return 0;
}
