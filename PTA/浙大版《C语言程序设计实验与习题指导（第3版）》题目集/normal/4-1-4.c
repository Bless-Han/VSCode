#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int k = 0;
	int sum = 0;
	while (n){
		k++;
		sum += n % 10;
		n /= 10;
	}
	printf("%d %d\n", k, sum);
	return 0;
}
