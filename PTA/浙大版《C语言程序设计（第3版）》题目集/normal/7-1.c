#include <stdio.h>

void swap( int *a, int j);
int main(void)
{
	int n;
	scanf("%d", &n);
	int a[n];
	int temp = n;
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
	for (int i = 0; i < n - 1; n--) {
		for (int j = 0; j < n - 1; j++) {
			if (a[j] < a[j + 1]) swap( a, j);
		}
	}
	for (int i = 0; i < temp; i++) {
		if (i != 0) printf(" ");
		printf("%d", a[i]);
	}
	return 0;
}
void swap( int *a, int j)
{
	int temp = a[j];
	a[j] = a[j + 1];
	a[j + 1] = temp;
}
