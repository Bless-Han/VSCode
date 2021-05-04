#include <stdio.h>

int main(void)
{
	double elec, cost;
	scanf("%lf", &elec);

	if (elec >= 0){
		if (elec > 50) 
			cost = 50 * 0.53 + (elec - 50) * (0.53 + 0.05);
		else 
			cost = 0.53 * elec;
		printf("cost = %0.2lf\n", cost);
	} else {
		printf("Invalid Value!\n");
	}
	return 0;
}
