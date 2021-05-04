#include <stdio.h>

int main(void)
{
	double bill, result;
	scanf("%lf", &bill);
	if (bill <= 1600) result = bill * 0;
	else if (bill <= 2500) result = (bill - 1600) * 0.05;
	else if (bill <= 3500) result = (bill - 1600) * 0.10;
	else if (bill <= 4500) result = (bill - 1600) * 0.15;
	else result = (bill - 1600) * 0.20;
	printf("%0.2lf\n", result);
	return 0;
}
