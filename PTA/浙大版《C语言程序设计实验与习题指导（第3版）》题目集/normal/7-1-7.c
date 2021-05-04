#include <stdio.h>

int main(void)
{
	int n, x, i, a;
	scanf("%d%d", &n, &x);
	for (i = 0; i < n; i++) {
		scanf("%d", &a);
		if (a == x)
			break;
	}
	if (i < n)
		printf("%d\n", i);
	else 
		printf("Not Found\n");
	return 0;
}
