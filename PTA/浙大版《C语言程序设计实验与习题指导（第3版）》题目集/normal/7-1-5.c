#include <stdio.h>
#define MAX_N 10

void swap(int *x, int i, int j)
{
	int temp = x[i];
	x[i] = x[j];
	x[j] = temp;
}
int main(void)
{
	int n;
	scanf("%d", &n);
	int a[MAX_N];
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	int index;
	for (int i = 0; i < n; i++) {
		index = i;
		for (int j = i + 1; j < n; j++) {
			if (a[j] > a[index])
				index = j;
		}
		if (index != i)
			swap(a, i, index);
	}
	for (int i = 0; i < n; i++) {
		if (i != 0)
			printf(" ");
		printf("%d", a[i]);
	}
	printf("\n");
	return 0;
}
