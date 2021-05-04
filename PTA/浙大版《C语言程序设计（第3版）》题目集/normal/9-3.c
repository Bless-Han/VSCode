#include <stdio.h>
#include <math.h>

int main(void)
{
	double x1, y1, x2, y2;
	scanf("%lf %lf %lf %lf", &x1, &y1, &x2, &y2);
	double v1 = x1 + x2;
	double v2 = y1 + y2;
	if (fabs(v1) < 0.05) v1 = fabs(v1);
	if (fabs(v2) < 0.05) v2 = fabs(v2);
	printf("(%0.1lf, %0.1lf)\n", v1, v2);
	return 0;
}
