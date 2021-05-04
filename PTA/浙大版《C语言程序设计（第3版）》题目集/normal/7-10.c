#include <stdio.h>
#include <string.h>

const int MAX_N = 80;
int main(void)
{
	char c;
	scanf("%c", &c);
	getchar();
	char s[MAX_N + 1];
	for (int i = 0; (s[i] = getchar()) != '\n'; i++) { }
	int len = strlen(s);
	int index;
	for ( index = len - 1;  index >= 0;  index--) {
		if (s[index] == c) break;
	}
	if (index < 0) printf("Not Found\n");
	else printf("index = %d\n", index);
	return 0;
}
