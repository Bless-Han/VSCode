#include <stdio.h>

int main(void)
{
	int number, sum = 0;
	while (1){
		scanf("%d", &number);
		if (number <= 0)
			break;
		if (number % 2 == 1)
			sum += number;
	}
	printf("%d", sum);
	return 0;
}
