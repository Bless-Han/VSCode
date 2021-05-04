#include <stdio.h>

double mypow( double x, int n );

int main()
{
	double x;
	int n;

	scanf("%lf %d", &x, &n);
	printf("%f\n", mypow(x, n));

	return 0;
}

/* 你的代码将被嵌在这里 */
double mypow( double x, int n )
{
	double ret=1;
	for (int i = 0; i < n; i++) ret*=x;
	return ret;
}
/*
实验2-4-5 简单实现x的n次方 (10分)

本题要求实现一个计算x​n​​（n≥0）的函数。
函数接口定义：

double mypow( double x, int n );

函数mypow应返回x的n次幂的值。题目保证结果在双精度范围内。
*/
