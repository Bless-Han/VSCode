#include <stdio.h>
#include <math.h>

double funcos( double e, double x );

int main()
{    
    double e, x;

    scanf("%lf %lf", &e, &x);
    printf("cos(%.2f) = %.6f\n", x, funcos(e, x));

    return 0;
}

/* 你的代码将被嵌在这里 */
double funcos( double e, double x )
{
	double ret = 0;
	double fact = 1;
	double j = 0;
	double sign = 1;
	double xx = 1;
	int i;
	for (i = 0; fabs(xx / fact) >= e; i += 2){
		ret += xx / fact * sign;
		sign *= -1;
		for (int i = 0; i < 2; i++) {
			j++;
			fact *= j;
			xx *= x;
		}
	}
	ret += xx / fact * sign;
	return ret;
}
