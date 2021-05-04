#include <stdio.h>

int main(void)
{
	double x;
	scanf("%lf", &x);
	double r;
	if (x == 0)
		r = 0;
	else 
		r = 1 / x;
	printf("f(%0.1lf) = %0.1lf\n", x, r);
	return 0;
}
