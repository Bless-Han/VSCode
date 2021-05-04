#include <stdio.h>

int main(void)
{
	int m, n;
	scanf("%d %d", &m, &n);
	int a[n][n];
	int temp;
	for (int i = 0; i < n; i++) {
		for (int j = 0, temp = m; j < n; j++, temp++) {
			for ( ; temp >= n; temp -= n) ;
			scanf("%d", &a[temp][i]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d ", a[j][i]);
		}
		printf("\n");
	}
	return 0;
}
