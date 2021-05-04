#include <stdio.h>
#include <math.h>

int main(void)
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	double perimeter = a + b + c;
	double s = perimeter / 2;
	double area = sqrt(s * (s - a) * (s - b) * (s - c));
	if (isnan(area) || area == 0) 
	   printf("These sides do not correspond to a valid triangle\n");
	else 
		printf("area = %0.2lf; perimeter = %0.2lf\n", area, perimeter);
	return 0;
}
