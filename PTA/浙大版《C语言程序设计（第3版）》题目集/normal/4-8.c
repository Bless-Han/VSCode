#include <stdio.h>

int main(void)
{
	double hi, n;
	scanf("%lf %lf", &hi, &n);
	double sum = 0;
	for (int i = 0; i < n; i++) {
		if (i == 0) sum += hi;
		else sum += hi * 2;
		hi /= 2;
	}
	if (n == 0) hi = 0;
	printf("%0.1lf %0.1lf\n", sum, hi);
	return 0;
}
