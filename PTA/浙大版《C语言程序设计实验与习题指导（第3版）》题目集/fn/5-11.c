#include <stdio.h>

int gcd( int x, int y );

int main()
{
    int x, y;

    scanf("%d %d", &x, &y);
    printf("%d\n", gcd(x, y));

    return 0;
}

/* 你的代码将被嵌在这里 */
int gcd( int x, int y )
{
	if (y % x == 0) return x;
	return gcd(y % x, x);
}
