#include <stdio.h>
#define APPLE 3
#define PEAR 2.5
#define ORANGE 4.1
#define GRAPE 10.2

int main(void)
{
	int n = 5;
	printf("[1] apple\n");
	printf("[2] pear\n");
	printf("[3] orange\n");
	printf("[4] grape\n");
	printf("[0] exit\n");
	for (int i = 0; i < 5; i++) {
		int a;
		scanf("%d", &a);
		double price;
		if (a == 0) break;
		else if (a == 1) price = APPLE;
		else if (a == 2) price = PEAR;
		else if (a == 3) price = ORANGE;
		else if (a == 4) price = GRAPE;
		else price == 0;
		printf("price = %0.2lf\n", price);
		price = 0;
	}
	return 0;
}
