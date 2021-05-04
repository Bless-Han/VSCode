#include <stdio.h>

int main(void)
{
	printf("152 = %d + %d*10 + %d*100\n", 152 % 10, 152 % 100 / 10, 152 / 100);
	return 0;
}
