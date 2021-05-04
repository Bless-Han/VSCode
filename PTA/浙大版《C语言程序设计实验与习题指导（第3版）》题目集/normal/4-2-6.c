#include <stdio.h>

void pr(int n)
{
	char c = 'A';
	for (int i = n; i > 0; i--) {
		for (int j = 0; j < i; j++) {
			printf("%c ", c);
			c++;
		}
		printf("\n");
	}
}
int main(void)
{
	int n;
	scanf("%d", &n);
	pr(n);
	return 0;
}
