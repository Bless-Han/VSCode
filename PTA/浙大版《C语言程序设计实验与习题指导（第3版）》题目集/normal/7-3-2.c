#include <stdio.h>
#define N 80

int search(char *s, char c)
{
	int ret = -1;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == c){
			ret = i;
		}
	}
	return ret;
}
int main(int argc, char *argv[])
{
	int c;
	scanf("%c\n", &c);
	char s[N + 1];
	int i = 0;
	while ((s[i++] = getchar()) != '\n');
	i--;
	s[i--] = '\0';
	int index = 0;
	if ((index = search(s, c)) != -1)
		printf("index = %d\n", index);
	else
		printf("Not Found\n");
	return 0;
}
