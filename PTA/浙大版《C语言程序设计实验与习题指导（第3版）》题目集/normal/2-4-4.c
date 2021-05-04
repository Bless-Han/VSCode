#include <stdio.h>

int fact(int n);
int main(void)
{
	int n;
	scanf("%d", &n);
	double sum = 0;
	for (int i = 0; i < n; i++) {
		sum += fact(i + 1);
	}
	printf("%0.0lf\n", sum);
	return 0;
}
int fact(int n)
{
	if (n == 0) return 1;
	return n * fact(n - 1);
}
