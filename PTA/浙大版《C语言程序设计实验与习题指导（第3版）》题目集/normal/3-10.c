#include <stdio.h>

int main(void)
{
	int a, b;
	scanf("%d %d", &a, &b);
	if (1.0 * (a - b) / b >= 0.5)
		printf("Exceed %0.0lf%%. License Revoked\n", 1.0 * (a - b) / b * 100);
	else if (1.0 * (a - b) / b >= 0.1)   
		printf("Exceed %0.0lf%%. Ticket 200\n", 1.0 * (a - b) / b * 100);
	else 
		printf("OK\n");
	return 0;
}
