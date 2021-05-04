#include <stdio.h>
#define MAX_N 200

int memory[MAX_N] = {0};
int fib(int i);
int main(void)
{
	int n;
	scanf("%d", &n);
	int i = 1;
	for (i = 0; 1; i++) {
		if (fib(i) >= n)
			break;
	}
	printf("%d", i);
	return 0;
}
int fib(int i)
{
	if (i <= 1) return i;
	if (memory[i] != 0) return memory[i];
	return memory[i] = fib(i - 1) + fib(i - 2);
}
