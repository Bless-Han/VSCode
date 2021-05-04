#include <stdio.h>
#define NUM 10

int main(void)
{
	int n;
	scanf("%d", &n);
	int a[n];
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
	int bottle[NUM] = {0};
	for (int i = 0; i < n; i++) {
		while (a[i] != 0) {
			bottle[a[i] % 10]++;
			a[i] /= 10;
		}
	}
	int m = 0;
	for (int i = 0; i < NUM; i++) if (bottle[i] > m) m = bottle[i];
	printf("%d:", m);
	for (int i = 0; i < NUM; i++) if (bottle[i] == m) printf(" %d", i);
	return 0;
}
