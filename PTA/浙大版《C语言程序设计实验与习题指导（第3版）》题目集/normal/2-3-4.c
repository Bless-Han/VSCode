#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int j = 1, flag = 1;
	double sum = 0;
	for (int i = 1; i <= n; i++) {
		sum += 1.0 / j * flag;
		j = j + 3;
		flag *= -1;
	}
	printf("sum = %0.3lf\n", sum);
	return 0;
}
