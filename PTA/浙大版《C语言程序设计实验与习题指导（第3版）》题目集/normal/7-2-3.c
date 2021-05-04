#include <stdio.h>

int main(int argc, char *argv[])
{
	int flag = 0;
	int m, n;
	scanf("%d %d", &m, &n);
	int a[m][n];
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	for (int i = 1; i < m - 1; i++) {
		for (int j = 1; j < n - 1; j++) {
			if (a[i][j] > a[i - 1][j] && \
					a[i][j] > a[i + 1][j] && \
					a[i][j] > a[i][j - 1] && \
					a[i][j] > a[i][j + 1]){
				flag = 1;
				printf("%d %d %d\n", a[i][j], i + 1, j + 1);
			}
		}
	}
	if (flag == 0) {
		printf("None %d %d\n", m, n);
	}
	return 0;
}
