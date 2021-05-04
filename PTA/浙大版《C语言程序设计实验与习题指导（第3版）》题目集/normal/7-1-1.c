#include <stdio.h>
#define MAX_N 10

int main(void)
{
	int n;
	int a[MAX_N];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	int k;
	scanf("%d", &k);
	for (int i = n; i >= 0; i--) {
		if (k >= a[i - 1]){
			a[i] = k;
			break;
		}
		a[i] = a[i - 1];
	}
	for (int i = 0; i < n + 1; i++) {
		printf("%d ", a[i]);
	}
	return 0;
}
