#include <stdio.h>
#define MAX_N 10

int main(void)
{
	int n, a[MAX_N] = {0};
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (int i = 0; i < n - 1; i++) {
		if (i % 3 != 0) printf(" ");
		printf("%d", a[i + 1] - a[i]);
		if ((i + 1) % 3 == 0) printf("\n");
	}
	return 0;
}
