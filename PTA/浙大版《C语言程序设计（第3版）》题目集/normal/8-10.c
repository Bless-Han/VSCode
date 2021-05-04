#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	double average;
	double sum, max, min;
	double temp;
	for (int i = 0; i < n; i++) {
		scanf("%lf", &temp);
		if (i == 0) sum = max = min = temp;
		else {
			sum += temp;
			if (max < temp) max = temp;
			if (min > temp) min = temp;
		}
	}
	printf("average = %0.2lf\n", sum / n);
	printf("max = %0.2lf\n", max);
	printf("min = %0.2lf\n", min);
	return 0;
}
