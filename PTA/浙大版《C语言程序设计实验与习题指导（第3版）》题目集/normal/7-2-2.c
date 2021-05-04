#include <stdio.h>

int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);
	int number;
	int sum = 0;
	for (int i = 0; i < n * n; i++) {
		int x = i / n;
		int y = i % n;
		scanf("%d", &number);
		if (x + 1 == n || y + 1 == n || x + y + 1 == n)
			continue;
		sum += number;
	}
	printf("%d\n", sum);
	return 0;
}
