#include <stdio.h>
#include <math.h>

int prime( int p );
void Goldbach( int n );

int main()
{
    int m, n, i, cnt;

    scanf("%d %d", &m, &n);
    if ( prime(m) != 0 ) printf("%d is a prime number\n", m);
    if ( m < 6 ) m = 6;
    if ( m%2 ) m++;
    cnt = 0;
    for( i=m; i<=n; i+=2 ) {
        Goldbach(i);
        cnt++;
        if ( cnt%5 ) printf(", ");
        else printf("\n");
    }

    return 0;
}

/* 你的代码将被嵌在这里 */
int prime( int p )
{
	int ret = 1;
	if (p >= 2){
		for (int i = 2; i <= sqrt(p); i++) {
			if (p % i == 0){
				ret = 0;
				break;
			}
		}
	} else ret = 0;
	return ret;
}
void Goldbach( int n )
{
	int p, q;
	int flag = 1;
	for (p = 2; p < n && flag; p++) {
		for (q = 3; q < n && flag; q++) {
			if (n == p + q && prime(p) && prime(q)){
				printf("%d=%d+%d", n, p, q);
				flag = 0;
			}
		}
	}
}
