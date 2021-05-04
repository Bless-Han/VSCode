#include <stdio.h>

void p(int n);
void s(int n);
int main(void)
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int middle = n / 2;
		if ((i + 1) <= middle) {
			s(middle - i);
			p((i + 1) * 2 - 1);
		} else {
			s(i - middle);
			p((n - i) * 2 - 1);
		}
		printf("\n");
	}
	return 0;
}
void p(int n)
{
	for (int i = 0; i < n; i++) printf("* ");
}
void s(int n)
{
	for (int i = 0; i < n; i++) printf("  ");
}
