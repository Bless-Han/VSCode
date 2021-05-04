#include <stdio.h>
#define N 80

int search(char *s, int n, char c)
{
	int ret = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == c){
			ret = 1;
			break;
		}
	}
	return ret;
}
void sort(char *s, int n)
{
	char temp;
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			if (s[j] > s[j + 1]){
				temp = s[j];
				s[j] = s[j + 1];
				s[j + 1] = temp;
			}
		}
	}
}
int main(int argc, char *argv[])
{
	char c;
	char s[N + 1];
	int n = 0;
	while ((c = getchar()) != '\n') {
		if (!search(s, n, c))
			s[n++] = c;
	}
	s[n] = '\0';
	sort(s, n);
	printf("%s\n", s);
	return 0;
}
