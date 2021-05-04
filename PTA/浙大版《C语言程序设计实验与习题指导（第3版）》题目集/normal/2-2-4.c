#include <stdio.h>
#include <math.h>

int main(void)
{
	double x, result = 0;
	scanf("%lf", &x);
	if (x >= 0) 
		result = pow(x, 0.5);
	else 
		result = pow(x + 1, 2) + 2 * x + 1 / x;
	printf("f(%0.2lf) = %0.2lf\n", x, result);
	return 0;
}
