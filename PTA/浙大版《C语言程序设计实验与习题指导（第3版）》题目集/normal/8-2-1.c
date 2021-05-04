#include <stdio.h>
#include <string.h>
#define N 80

int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);
	char s[N + 1];
	char min[N + 1];
	for (int i = 0; i < n; i++) {
		scanf("%s", s);
		if (i == 0)
			strcpy(min, s);
		if (strcmp(s, min) < 0)
			strcpy(min, s);
	}
	printf("Min is: %s\n", min);
	return 0;
}
