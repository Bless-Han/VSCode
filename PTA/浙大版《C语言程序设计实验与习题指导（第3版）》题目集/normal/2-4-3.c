#include <stdio.h>
#include <math.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	double sum = 0;
	for (int i = 0; i < n; i++) {
		sum += sqrt(i + 1);
	}
	printf("sum = %0.2lf\n", sum);
	return 0;
}
