#include <stdio.h>

int main(void)
{
	int n;
	int min;
	int number;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &number);
		if (i == 0) min = number;
		else if (number < min) min = number;
	}
	printf("min = %d\n", min);
	return 0;
}
