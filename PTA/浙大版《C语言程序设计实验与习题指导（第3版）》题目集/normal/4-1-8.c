#include <stdio.h>
#include <math.h>

int main(void)
{
	double esp, sum = 0;
	double fenmu = 1;
	int flag = 1;
	scanf("%lf", &esp);
	while (1 / fenmu > esp) {
		sum += 1 / fenmu * flag;
		fenmu += 3;
		flag *= -1;
	}
	sum += 1 / fenmu * flag;
	printf("sum = %0.6lf\n", sum);
	return 0;
}
