#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int a[n];
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
	int b[n];
	for (int i = 0; i < n; i++) b[i] = a[n - (i + 1)];
	for (int i = 0; i < n; i++) {
		if (i != 0) printf(" ");
		printf("%d", b[i]);
	}
	printf("\n");
	return 0;
}
