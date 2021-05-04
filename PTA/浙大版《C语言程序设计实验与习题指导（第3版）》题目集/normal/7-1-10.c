#include <stdio.h>

void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}
int main(void)
{
	int n, a[10], min = 0, max = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		if (a[i] < a[min]) min = i;
		if (a[i] > a[max]) max = i;
	}
	if (min == n - 1 || max == 0){
		swap(&a[min], &a[max]);
		swap(&min, &max);
	}
	swap(&a[0], &a[min]);
	swap(&a[n - 1], &a[max]);
	for (int i = 0; i < n; i++) {
		printf("%d ", a[i]);
	}
	return 0;
}
