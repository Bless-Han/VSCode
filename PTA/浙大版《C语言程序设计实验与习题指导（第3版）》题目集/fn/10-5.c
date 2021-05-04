#include <stdio.h>

double fn( double x, int n );

int main()
{
    double x;
    int n;

    scanf("%lf %d", &x, &n);
    printf("%.2f\n", fn(x,n));

    return 0;
}

/* 你的代码将被嵌在这里 */

double fn( double x, int n )
{
	int sign = 1;
	if (n % 2 == 0) sign = -1;
	double ret = 1;
	for (int i = 0; i < n; i++) {
		ret *= x;
	}
	if (n == 1) return x;
	return ret * sign + fn(x, n - 1);
}
