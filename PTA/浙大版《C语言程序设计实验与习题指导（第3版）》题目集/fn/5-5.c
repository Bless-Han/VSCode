#include <stdio.h>
#include <math.h>

int prime( int p );
int PrimeSum( int m, int n );

int main()
{
    int m, n, p;

    scanf("%d %d", &m, &n);
    printf("Sum of ( ");
    for( p=m; p<=n; p++ ) {
        if( prime(p) != 0 )
            printf("%d ", p);
    }
    printf(") = %d\n", PrimeSum(m, n));

    return 0;
}

/* 你的代码将被嵌在这里 */
int prime( int p )
{
	int ret = 1;
	if (p >= 2) {
		for (int i = 2; i <= sqrt(p); i++) {
			if (p % i == 0) {
				ret = 0;
				break;
			}
		}
	} else ret = 0;
	return ret;
}
int PrimeSum( int m, int n )
{
	int ret = 0;
	for ( ; m <= n; m++){
		if (prime(m) == 1) ret += m;
	}
	return ret;
}
