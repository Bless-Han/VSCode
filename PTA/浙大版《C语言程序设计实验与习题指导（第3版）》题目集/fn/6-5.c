#include <stdio.h>

int fib( int n );
void PrintFN( int m, int n );

int main()
{
    int m, n, t;

    scanf("%d %d %d", &m, &n, &t);
    printf("fib(%d) = %d\n", t, fib(t));
    PrintFN(m, n);

    return 0;
}

/* 你的代码将被嵌在这里 */
int fib( int n )
{
	if (n <= 1) return n;
	return fib(n - 1) + fib(n - 2);
}
void PrintFN( int m, int n )
{
	int flag = 0;
	for (int i = 0; 1; i++) {
		if (fib(i) > n) break;
		if(fib(i) >= m && fib(i) <= n){
			if (flag == 1) {
				printf(" ");
			}
			printf("%d", fib(i));
			flag = 1;
		}
	}
	if (flag == 0)
		puts("No Fibonacci number");
}
