#include <stdio.h>

int factorsum( int number );
void PrintPN( int m, int n );

int main()
{
    int m, n;

    scanf("%d %d", &m, &n);
    if ( factorsum(m) == m ) printf("%d is a perfect number\n", m);
    if ( factorsum(n) == n ) printf("%d is a perfect number\n", n);
    PrintPN(m, n);

    return 0;
}

/* 你的代码将被嵌在这里 */

int factorsum( int number )
{
	int ret = 0;
	for (int i = 1; i < number; i++) {
		if (number % i == 0)
			ret += i;
	}
	return ret;
}
void PrintPN( int m, int n )
{
	int flag = 0;
	for ( ; m <= n; m++){
		if (factorsum(m) == m){
			flag = 1;
			printf("%d = 1", m);
			for (int i = 2; i < m; i++) {
				if (m % i == 0) 
					printf(" + %d", i);
			}
			puts("");
		}
	}
	if (flag == 0)
		puts("No perfect number");
}
