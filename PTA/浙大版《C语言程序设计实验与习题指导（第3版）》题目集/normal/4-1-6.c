#include <stdio.h>

int main(void)
{
	double sum = 0;
	double fenzi = 2, fenmu = 1;
	double n;
	double temp;
	scanf("%lf", &n);
	for (int i = 0; i < n; i++) {
		sum += fenzi / fenmu;
		temp = fenzi;
		fenzi = fenzi + fenmu;
		fenmu = temp;
	}
	printf("%0.2lf\n", sum);
	return 0;
}
