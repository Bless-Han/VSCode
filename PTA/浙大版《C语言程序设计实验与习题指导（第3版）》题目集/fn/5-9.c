#include <stdio.h>

int narcissistic( int number );
void PrintN( int m, int n );

int main()
{
    int m, n;

    scanf("%d %d", &m, &n);
    if ( narcissistic(m) ) printf("%d is a narcissistic number\n", m);
    PrintN(m, n);
    if ( narcissistic(n) ) printf("%d is a narcissistic number\n", n);

    return 0;
}

/* 你的代码将被嵌在这里 */
#include <math.h>
int narcissistic( int number )
{
	int i;
	int temp = number;
	int sum = 0;
	for ( i = 0; temp; temp /= 10) i++;
	temp = number;
	for (int j = 0; j < i; j++, temp /= 10) {
		sum += pow(temp % 10, i);
	}
	if (sum == number) return 1;
	else return 0;
}
void PrintN( int m, int n )
{
	for( m++; m < n; m++)
		if (narcissistic(m)) printf("%d\n", m);
}

