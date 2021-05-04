#include <stdio.h>

int main(int argc, char *argv[])
{
	int m, n;
	scanf("%d%d", &m, &n);
	int a[6][6];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[i][(j + m) % n]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d ", a[i][j]);
		}
		printf("\n");
	}

	return 0;
}
