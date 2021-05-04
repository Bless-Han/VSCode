#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int rabbit = 1;
	int last_m = 0; // Last month rabbit add numbers.
	int temp;
	int month = 1;
	while (rabbit < n) {
		if (month == 1) month = 2;
		month++;
		temp = rabbit;
		rabbit += rabbit - last_m;
		last_m = rabbit - temp;
	}
	printf("%d\n", month);
	return 0;
}
