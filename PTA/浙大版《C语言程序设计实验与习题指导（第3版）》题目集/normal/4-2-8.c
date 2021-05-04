#include <stdio.h>

void pr(int n){
	if (n / 10 == 0) printf("%d ", n);
	else {
		pr(n / 10);
		printf("%d ", n % 10);
	}
}
int main(void)
{
	int n;
	scanf("%d", &n);
	pr(n);
	return 0;
}
