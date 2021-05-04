#include <stdio.h>
#define N 10

void add(int a[], int x, int y, int i, int n)
{
	while (i < n * n){
		while (y + 1 < n && a[x * n + y + 1] == 0)
			a[x * n + y++] = i++;
		while (x + 1 < n && a[(x + 1) * n + y] == 0)
			a[x++ * n + y] = i++;
		while (y > 0 && a[x * n + y - 1] == 0)
			a[x * n + y--] = i++;
		while (a[(x - 1) * n + y] == 0)
			a[x-- * n + y] = i++;
	}
	a[x * n + y] = i;
}
int main(int argc, char *argv[])
{
	int a[N * N] = {0};
	int n;
	scanf("%d", &n);
	int x, y;
	x = y = 0;
	int i = 1;
	add(a, x, y, i, n);
	for (int i = 0; i < n; i++) {
		if (i != 0)
			printf("\n");
		for (int j = 0; j < n; j++) {
			printf("%3d", a[i * n + j]);
		}
	}
	return 0;
}
