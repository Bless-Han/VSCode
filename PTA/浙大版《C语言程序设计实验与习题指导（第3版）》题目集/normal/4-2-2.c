#include <stdio.h>

double fact(int n)
{
	if (n == 0) return 1;
	return n * fact(n - 1);
}
int main(void)
{
	double sum = 1;
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		sum += 1 / fact(i + 1);
	}
	printf("%0.8lf\n", sum);
	return 0;
}
