#include <stdio.h>
#include <math.h>

int main(void)
{
	int m, n;
	scanf("%d %d", &m, &n);
	double sum = 0;
	for ( ; m <= n; m++) {
		sum += pow(m, 2) + 1.0 / m;
	}
	printf("sum = %0.6lf\n", sum);
	return 0;
}
