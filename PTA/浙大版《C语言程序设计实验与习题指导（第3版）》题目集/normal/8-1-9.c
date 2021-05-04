#include <stdio.h>

int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);
	double sum = 0;
	double max = 0;
	double min = 100;
	double temp;
	for (int i = 0; i < n; i++) {
		scanf("%lf", &temp);
		if (max < temp)
			max = temp;
		if (min > temp)
			min = temp;
		sum += temp;
	}
	printf("average = %0.2lf\n", sum / n);
	printf("max = %0.2lf\n", max);
	printf("min = %0.2lf\n", min);
	return 0;
}
