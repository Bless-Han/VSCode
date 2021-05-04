#include <stdio.h>

int main(int argc, char *argv[])
{
	int m, n;
	scanf("%d %d", &m, &n);
	int a[m][n];
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	int sum;
	for (int i = 0; i < m; i++) {
		sum = 0;
		for (int j = 0; j < n; j++) {
			sum += a[i][j];
		}
		printf("%d\n", sum);
	}
	return 0;
}
