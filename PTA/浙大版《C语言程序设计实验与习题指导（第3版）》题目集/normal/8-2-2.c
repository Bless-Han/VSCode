#include <stdio.h>
#include <string.h>
#define N 80

int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);
	char s[N + 1];
	char longest[N + 1] = {'\0'};
	for (int i = 0; i < n; i++) {
		scanf("%s", s);
		if (strlen(s) > strlen(longest))
			strcpy(longest, s);

	}
	printf("The longest is: %s\n", longest);
	return 0;
}
