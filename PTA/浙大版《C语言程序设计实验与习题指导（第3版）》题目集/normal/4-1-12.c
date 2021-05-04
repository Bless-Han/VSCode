#include <stdio.h>
#define RESULT 495

int big, small;
void swap(int *a, int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}
int change(int n)
{
	int a, b, c;
	a = n / 100;
	b = n % 100 / 10;
	c = n % 10;
	if (a < b) swap (&a, &b);
	if (a < c) swap (&a, &c);
	if (b < c) swap (&b, &c);
	big = a * 100 + b * 10 + c;
	small = c * 100 + b * 10 + a;
	return big - small;
}
int main(void)
{
	int n;
	scanf("%d", &n);
	int number = n;
	int i = 1;
	while (number != 495 || i == 1) {
		number = change(number);
		printf("%d: %d - %d = %d\n", i, big, small, number);
		i++;
	}
	return 0;
}
