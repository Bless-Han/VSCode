#include <stdio.h>
#define MAX_N 10

int main(void)
{
	int n;
	scanf("%d", &n);
	int a[MAX_N];
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (int i = n - 1; i >= 0; i--) {
		if (i != n - 1)
			printf(" ");
		printf("%d", a[i]);
	}
	printf("\n");
	return 0;
}
