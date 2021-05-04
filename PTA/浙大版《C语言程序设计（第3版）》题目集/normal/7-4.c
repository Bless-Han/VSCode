#include <stdio.h>

const int MAX_N = 21;
void pd(int *a, int n_a, int *b, int n_b, int *c, int *n_c);
int main(void)
{
	int n_a;
	scanf("%d", &n_a);
	int a[n_a];
	for (int i = 0; i < n_a; i++) scanf("%d", &a[i]);
	int n_b;
	scanf("%d", &n_b);
	int b[n_b];
	for (int i = 0; i < n_b; i++) scanf("%d", &b[i]);
	int c[MAX_N];
	int n_c = 0;
	pd (a, n_a, b, n_b, c, &n_c);
	pd (b, n_b, a, n_a, c, &n_c);
	for (int i = 0; i < n_c; i++) {
		if (i != 0) printf(" ");
		printf("%d", c[i]);
	}
	return 0;
}
void pd(int *a, int n_a, int *b, int n_b, int *c, int *n_c)
{
	int flag = 1;
	for (int i = 0; i < n_a; i++) {
		flag = 1;
		for (int j = 0; j < n_b; j++) {
			if (a[i] == b[j]) {
				flag = 0;
				break;
			}
		}
		if (flag){
			for (int k = 0; k < *n_c; k++) {
				if (a[i] == c[k]) {
					flag = 0;
					break;
				}
			}
			if (flag) {
				c[*n_c] = a[i];
				(*n_c)++;
			}
		}
	}
}
