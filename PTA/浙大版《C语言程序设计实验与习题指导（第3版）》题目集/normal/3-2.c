#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int y;
	if (n > 0) y = 1;
	else if (n < 0) y = -1;
	else y = 0;
	printf("sign(%d) = %d", n, y);
	return 0;
}
