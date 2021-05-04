#include <stdio.h>
#include <math.h>
#define N 80

int x(char c)
{
	int ret;
	if (c >= '0' && c <= '9')
		ret = c - '0';
	else if (c >= 'a' && c <= 'f')
		ret = c - 'a' + 10;
	else 
		ret = c - 'A' + 10;
	return ret;
		
}
double change(char *s, int negative)
{
	double ret = 0;
	int n = 0;
	for (n = 0; s[n] != '\0'; n++) ;
	for (int i = 0; i < n; i++) {
		ret += pow(16, n - i - 1) * x(s[i]);
	}
	return ret * negative;
}
int main(int argc, char *argv[])
{
	char c;
	char s[N + 1];
	int i = 0;
	int flag = 0;
	int negative = 1;
	while ((c = getchar()) != '#') {
		if (flag == 0 && c == '-'){
			negative = -1;
			flag = 1;
			continue;
		}
		if ((c >= '0' && c <= '9') || (c >= 'A' && c <= 'F') || \
				(c >= 'a' && c <= 'f')) {
			s[i++] = c;
			flag = 1;
		}
	}
	s[i] = '\0';
	double number = change(s, negative);
	if (i == 0)
		number = 0;
	printf("%0.0lf\n", number);
	return 0;
}
