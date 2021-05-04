#include <stdio.h>
int n, a[4];

void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}
void change(void)
{
	for (int i = 3; i >= 0; i--) {
		a[i] = n % 10;
		a[i] = (a[i] + 9) % 10;
		n /= 10;
	}
	swap(&a[0], &a[2]);
	swap(&a[1], &a[3]);
}
int main(void)
{
	scanf("%d", &n);
	change();
	printf("The encrypted number is ");
	for (int i = 0; i < 4; i++) {
		printf("%d", a[i]);
	}
	printf("\n");
	return 0;
}

