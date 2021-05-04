#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int sum = 0, temp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &temp);
			if (j != (n - 1) && i != (n - 1) && (i + j ) != (n - 1)) sum += temp;
		}
	}
	printf("%d\n", sum);
	return 0;
}
