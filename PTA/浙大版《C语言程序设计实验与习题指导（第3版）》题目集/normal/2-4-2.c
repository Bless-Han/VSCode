#include <stdio.h>
#include <math.h>
#define NUMBER 3

int main(void)
{
	int i;
	scanf("%d", &i);
	for (int j = 0; j <= i; j++) {
		printf("pow(%d,%d) = %0.0lf\n", NUMBER, j, pow(NUMBER, j));
	}
	return 0;
}
