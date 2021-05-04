#include <stdio.h>
#include <math.h>
#define N 80

int main(int argc, char *argv[])
{
	char c;
	char s[N + 1];
	int n = 0;
	while ((c = getchar()) != '\n'){
		if (c >= '0' && c <= '9')
			s[n++] = c;
	}
	double number = 0;
	for (int i = 0; i < n; i++) {
		number += pow(10, n - i - 1) * (s[i] - '0');
	}
	printf("%0.0lf\n", number);
	return 0;
}
