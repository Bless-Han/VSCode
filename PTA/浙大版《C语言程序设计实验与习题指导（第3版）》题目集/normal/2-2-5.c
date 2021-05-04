#include <stdio.h>
#define N 4

int main(void)
{
	int sum = 0;
	for (int i = 0; i < N; i++) {
		int temp;
		scanf("%d", &temp);
		sum += temp;
	}
	printf("Sum = %d; Average = %0.1lf\n", sum, 1.0 * sum / N);
	return 0;
}
