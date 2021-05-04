#include <stdio.h>
#include <math.h>

int prime(int n)
{
	int ret = 1;
	for (int i = 2; i <= sqrt(n); i++) {
		if (n % i == 0){
			ret = 0;
			break;
		}
	}
	return ret;
}
int main(void)
{
	int n;
	scanf("%d", &n);
	int i, j;
	for (i = 2; i <= n / 2; i++) {
		j = n - i;
		if (prime(i) && prime(j)){
			printf("%d = %d + %d\n", n, i, j);
			break;
		}
	}
	return 0;
}
