#include <stdio.h>
#include <math.h>

int main(void)
{
	double money, year, rate;
	scanf("%lf %lf %lf", &money, &year, &rate);
	double interest = money * pow((1 + rate), year) - money;
	printf("interest = %0.2lf\n", interest);
	return 0;
}
