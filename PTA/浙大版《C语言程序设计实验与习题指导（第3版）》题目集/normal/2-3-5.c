#include <stdio.h>

int main(void)
{
	int lower, upper;
	scanf("%d %d", &lower, &upper);
	if (lower <= upper){
		printf("fahr celsius\n");
		for ( ; lower <= upper; lower += 2) {
			printf("%d%6.1lf\n", lower, 5.0 * (lower - 32) / 9);
		}
	} else {
		printf("Invalid.\n");
	}
	return 0;
}
