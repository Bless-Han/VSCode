#include <stdio.h>

int beggest(int a, int b);
int least(int a, int b);
int main(void)
{
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d %d\n", beggest(a, b), least(a, b));
	return 0;
}
int beggest(int a, int b)
{
	if (a % b == 0) return b;
	return beggest(b, a % b);
}
int least(int a, int b)
{
	return a / beggest(a, b) * b;
}
