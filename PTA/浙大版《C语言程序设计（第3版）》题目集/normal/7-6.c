#include <stdio.h>
#define MAX_N 500

int main(void)
{
	char a[MAX_N];
	int i;
	for (i = 0; (a[i] = getchar()) != '\n'; i++) ;
	a[i] = '\0';
	int count = 0;
	for (int j = 0; j < i; j++) {
		if (a[j] >= 'A' && a[j] <= 'Z' && a[j] != 'A' && a[j] != 'E' && a[j] != 'I' && a[j] != 'O' && a[j] != 'U')
			count++;
	}
	printf("%d\n", count);
	return 0;
}
