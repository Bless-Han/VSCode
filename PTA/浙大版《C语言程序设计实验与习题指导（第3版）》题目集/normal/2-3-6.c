#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	double sum = 1, flag = -1;
	for (int i = 2; i <= n; i++) {
		sum += flag * i / (i * 2 - 1);
		flag *= -1;
	}
	printf("%0.3lf", sum);
	return 0;
}
