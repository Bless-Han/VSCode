#include <stdio.h>

int main(void)
{
	int soldier = 0;
	while (!(soldier % 5 == 1 && soldier % 6 == 5 && soldier % 7 == 4 && soldier % 11 == 10)) soldier++;
	printf("%d\n", soldier);
	return 0;
}
