#include <stdio.h>
#define MAX_N 10000

int bottle[10] = {0};
int big = 0;
void change(int x)
{
	if (x == 0) bottle[0]++;
	while (x){
		bottle[x % 10]++;
		x /= 10;
	}
}
int main(void)
{
	int n;
	int a[MAX_N];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		change(a[i]);
	}
	for (int i = 0; i < 10; i++) {
		if (bottle[i] > big)
			big = bottle[i];
	}
	printf("%d:", big);
	for (int i = 0; i < 10; i++) {
		if (bottle[i] == big)
			printf(" %d", i);
	}

	return 0;
}
