#include <stdio.h>

int flag = 0;
int panduan(int x)
{
	int sum = 0;
	for (int i = 1; i <= x / 2; i++) {
		if (x % i == 0)
			sum += i;
	}
	return sum == x;
}
void pr(int x)
{
	printf("%d = ", x);
	for (int i = 1; i <= x / 2; i++) {
		if (x % i == 0){
			if (i != 1)
				printf(" + ");
			printf("%d", i);
		}
	}
	printf("\n");
}
int main(void)
{
	int m, n;
	scanf("%d %d", &m, &n);
	for ( ; m <= n; m++){
		if (panduan(m)){
			flag = 1;
			pr(m);
		}
	}
	if (flag == 0)
		printf("None\n");
	return 0;
}
