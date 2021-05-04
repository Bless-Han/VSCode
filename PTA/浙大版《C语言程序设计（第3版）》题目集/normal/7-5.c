#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int a[n][n];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	int flag;
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			flag = 1;
			for (int k = 0; k < n; k++) {
				if (a[i][j] < a[i][k] && j != k){
					flag = 0;
					break;
				}
			}
			for (int k = 0; k < n; k++) {
				if (a[i][j] > a[k][j] && i != k) {
					flag = 0;
					break;
				}
			}
			if (flag) goto end;
		}
	}
end:
	if (flag) printf("%d %d\n", i, j);
	else printf("NONE\n");
	return 0;
}
