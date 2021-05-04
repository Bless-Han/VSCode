#include <stdio.h>

void yanghui(int n);
void space(int n);
int f(int row, int col);
int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);
	yanghui(n);
	return 0;
}
void yanghui(int n)
{
	for (int i = 0; i < n; i++) {
		space(n - i - 1);
		for (int j = 0; j <= i; j++) {
			printf("%4d",f(i, j));
		}
		printf("\n");
	}
}
void space(int n)
{
	for (int i = 0; i < n; i++) {
		printf(" ");
	}
}
int f(int row, int col)
{
	if (col == 0 || col == row) return 1;
	return f(row - 1, col - 1) + f(row - 1, col);
}
