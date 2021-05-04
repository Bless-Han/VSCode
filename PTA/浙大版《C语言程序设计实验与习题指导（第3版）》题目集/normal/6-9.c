#include <stdio.h>
#define MAX_N 500

void read(char *s)
{
	int i;
	for (i = 0; (s[i] = getchar()) != '\n'; i++) ;
	s[i] = '\0';
}
int count(char *s)
{
	int space = 0;
	int flag = 0;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == ' ')
			flag = 0;
		if (s[i] != ' ' && flag == 0){
			flag = 1;
			space ++;
		}
	}
	return space;
}
int main(void)
{
	char s[MAX_N];
	read(s);
	printf("%d\n", count(s));
	return 0;
}
