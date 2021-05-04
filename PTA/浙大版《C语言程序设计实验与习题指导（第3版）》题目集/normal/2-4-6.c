#include <stdio.h>
#include <math.h>
#define K 2

int main(void)
{
	int n;
	scanf("%d", &n);
	double result = 0;
	for (int i = 0; i < n; i++) {
		result += pow(K, i + 1);
	}
	printf("result = %0.0lf\n", result);
	return 0;
}
