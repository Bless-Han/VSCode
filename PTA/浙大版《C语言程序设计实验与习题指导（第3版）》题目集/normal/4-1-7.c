#include <stdio.h>

int f(int a, int n);
int main(void)
{
	int a, n;
	int s = 0;
	scanf("%d %d", &a, &n);
	for (int i = 0; i < n; i++) {
		s += f(a, i + 1);
	}
	printf("s = %d\n", s);
	return 0;
}
int f(int a, int n)
{
	int ret = 0;
	for (int i = 0; i < n; i++) {
		ret += a;
		a *= 10;
	}
	return ret;
}
