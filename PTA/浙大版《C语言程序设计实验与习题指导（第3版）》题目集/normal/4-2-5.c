#include <stdio.h>
#include <math.h>

int shuixian(int x, int n)
{
	int k = 0;
	int temp = x;
	int sum = 0;
	int a;
	int b;
	for (int i = 0; i < n; i++) {
		a = temp % 10;
		b = 1;
		for (int j = 0; j < n; j++) {
			b *= a;
		}
		sum += b;
		temp /= 10;
	}
	return sum == x;
}
int main(void)
{
	int n;
	scanf("%d", &n);
	int a = pow(10, n - 1);
	int b = pow(10, n);
	for ( ; a < b; a++) {
		if (shuixian(a, n)) 
			printf("%d\n", a);
	}
	return 0;
}
