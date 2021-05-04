#include <stdio.h>
#define MAX_N 20

int read(int *x)
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &x[i]);
	}
	return n;
}
int look(int *x, int xN, int *y, int yN, int k)
{
	int ret = 1;
	for (int i = 0; i < xN; i++) {
		if (x[i] == k){
			ret = 0;
			goto END;
		}
	}
	for (int i = 0; i < yN; i++) {
		if (y[i] == k){
			ret = 0;
			goto END;
		}
	}
END:
	return ret;
}
int main(void)
{
	int a[MAX_N], b[MAX_N];
	int aN = read(a);
	int bN = read(b);
	int c[MAX_N];
	int cN = 0;
	for (int i = 0; i < aN; i++) {
		if (look(b, bN, c, cN, a[i])) {
			c[cN++] = a[i];
		}
	}
	for (int i = 0; i < bN; i++) {
		if (look(a, aN, c, cN, b[i])) {
			c[cN++] = b[i];
		}
	}
	for (int i = 0; i < cN; i++) {
		if (i != 0)
			printf(" ");
		printf("%d", c[i]);
	}
	printf("\n");
	return 0;
}
