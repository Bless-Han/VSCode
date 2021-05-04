#include <stdio.h>
#include <math.h>

int search( int n );

int main()
{
    int number;

    scanf("%d",&number);
    printf("count=%d\n",search(number));

    return 0;
}


/* 你的代码将被嵌在这里 */

int search( int n )
{
	int ret = 0;
	int k = 9;
	int a, b, c;
	while (1){
		if (k * k < 101) {
			k++;
			continue;
		}
		if (k * k > n) break;
		a = (k * k) % 10;
		b = (k * k) % 100 / 10;
		c = (k * k) / 100;
		if (a == b || a == c || b == c)
			ret++;
		k++;
	}
	return ret;
}
