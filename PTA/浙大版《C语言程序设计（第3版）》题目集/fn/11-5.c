#include <stdio.h>

#define MAXS 10

char *match( char *s, char ch1, char ch2 );

int main()
{
	char str[MAXS], ch_start, ch_end, *p;

	scanf("%s\n", str);
	scanf("%c %c", &ch_start, &ch_end);
	p = match(str, ch_start, ch_end);
	printf("%s\n", p);

	return 0;
}

#include <string.h>
char *match( char *s, char ch1, char ch2 )
{
	char *ret = s;
	int len = strlen(s);
	int i;
	for (i = 0; i < len; i++) {
		if (s[i] == ch1)  break;
	}
	ret = &s[i];
	if (i < len) {
		int j = i;
		for (; j < len; j++) {
			if ((s[j] == ch2) || (j == len - 1)) {
				printf("%0.*s\n", j - i + 1, ret);
				break;
			}
		}
	} else printf("\n");
	return ret;
}

/*
习题11-5 指定位置输出字符串 (20分)

本题要求实现一个函数，对给定的一个字符串和两个字符，打印出给定字符串中从与第一个字符匹配的位置开始到与第二个字符匹配的位置之间的所有字符。
函数接口定义：

char *match( char *s, char ch1, char ch2 );

函数match应打印s中从ch1到ch2之间的所有字符，并且返回ch1的地址。
裁判测试程序样例：



输入样例1：

program
r g

输出样例1：

rog
rogram

输入样例2：

program
z o

输出样例2：

(空行)
	(空行)

	输入样例3：

	program
	g z

	输出样例3：

	gram
	gram
*/
