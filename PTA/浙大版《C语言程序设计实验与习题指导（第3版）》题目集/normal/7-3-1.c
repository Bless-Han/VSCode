#include <stdio.h>
#define N 80

int main(int argc, char *argv[])
{
	char s[N + 1];
	int i = 0;
	while ((s[i++] = getchar()) != '\n') ;
	i--;
	s[i--] = '\0';
	for ( ; i >= 0; i--) {
		printf("%c", s[i]);
	}
	printf("\n");
	return 0;
}
