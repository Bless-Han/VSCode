#include <stdio.h>
#define MAX_N 80

int main(void)
{
	char a[MAX_N + 1];
	int i;
	for (i = 0; (a[i] = getchar()) != '\n'; i++) ;
	a[i] = '\0';
	for (int j = 0; j < i; j++) {
		if (a[j] >= 'A' && a[j] <= 'Z') {
			a[j] = ('Z' - 'A') - (a[j] - 'A') + 'A';
		}
	}
	printf("%s\n", a);
	return 0;
}
