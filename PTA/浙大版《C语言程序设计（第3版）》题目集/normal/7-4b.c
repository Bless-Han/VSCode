#include <stdio.h>

int main(void)
{
	int m, n;
	scanf("%d %d", &m, &n);
	int a[m];
	for (int i = 0; i < m; i++) a[i] = 0;
	int temp;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &temp);
			a[i] += temp;
		}
	}
	for (int i = 0; i < m; i++) printf("%d\n", a[i]);
	return 0;
}
