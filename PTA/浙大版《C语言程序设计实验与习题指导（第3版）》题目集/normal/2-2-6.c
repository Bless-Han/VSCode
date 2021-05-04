#include <stdio.h>

int main(void)
{
	double x, y;
	scanf("%lf", &x);
	if (x == 10)
		y = 1 / x;
	else
		y = x;
	printf("f(%0.1lf) = %0.1lf\n", x, y);
	return 0;
}
