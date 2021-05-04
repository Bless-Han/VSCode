#include <stdio.h>
#include <math.h>

int prime(int x)
{
	int ret = 1;
	for (int i = 2; i <= sqrt(x); i++) {
		if (x % i == 0){
			ret = 0;
			break;
		}
	}
	return ret;
}
int main(void)
{
	int flag = 0;
	int n;
	int number;
	scanf("%d", &n);
	for (int i = 2; i <= n; i++) {
		number = pow(2, i) - 1;
		if (prime(number)) {
			flag = 1;
			printf("%d\n", number);
		}
	}
	if (flag == 0)
		printf("None\n");
	return 0;
}
