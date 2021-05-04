#include <stdio.h>

double fact(int n);
int main(void)
{
	int m, n;
	scanf("%d %d", &m, &n);
	double result = fact(n) / (fact(m) * fact(n - m));
	printf("result = %0.0lf\n", result);
	return 0;
}
double fact(int n)
{
	if (n == 0) return 1;
	return n * fact(n - 1);
}
