#include <stdio.h>

double fact(int i)
{
	if (i == 1) return i;
	return i * fact(i - 1);
}
double fact2(int i)
{
	if (i == 1) return 3;
	return (i * 2 + 1) * fact2(i - 1);
}
int main(void)
{
	double eps;
	scanf("%le", &eps);
	double x = 1;
	double pii2 = 1; // pi / 2
	int i = 0;
	do {
		if (i != 0){
			x = fact(i) / fact2(i);
			pii2 += x;
		}
		i++;
	} while (x > eps);
	printf("PI = %0.5lf\n", pii2 * 2);
	return 0;
}
