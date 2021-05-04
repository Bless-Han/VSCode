#include <stdio.h>

int main(void)
{
	double height, n;
	scanf("%lf %lf", &height, &n);
	double sum = 0;
	double bounce = 0;
	int i = 0;
	for (int i = 0; i < n; i++) {
		if (i == 0)
			sum += height;
		else 
			sum += height * 2;
		bounce = height = height / 2;
	}
	printf("%0.1lf %0.1lf\n", sum, bounce);
	return 0;
}
