#include <stdio.h>
#define N 80

int add(char *s, int j, char c){
	if (c >= 'A' && c <= 'Z'){
		int flag = 0;
		for (int i = 0; i < j; i++) {
			if (s[i] == c){
				flag = 1;
				break;
			}
		}
		if (flag == 0)
			s[j++] = c;
	}
	return j;
}
int main(int argc, char *argv[])
{
	char c;
	char s[N + 1];
	int i = 0;
	while ((c = getchar()) != '\n'){
		s[i++] = c;
	}
	s[i] = '\0';
	int n = i;
	char big[N + 1] = {0};
	int j = 0;
	for (int i = 0; i < n; i++) {
		j = add (big, j, s[i]);
	}
	big[j] = '\0';
	if (j)
		printf("%s\n", big);
	else
		printf("Not Found\n");
	return 0;
}
