#include <stdio.h>

int main(void)
{
	double sum = 0;
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		sum += 1.0 / i;
	}
	printf("sum = %0.6lf\n", sum);
	return 0;
}
