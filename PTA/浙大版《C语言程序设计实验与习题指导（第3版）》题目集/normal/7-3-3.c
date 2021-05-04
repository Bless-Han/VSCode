#include <stdio.h>

int judge(char c)
{
	int ret = 0;
	if ((c >= 'A' && c <= 'Z') && c != 'A' && c != 'E' && \
			c != 'I' && c != 'O' && c != 'U')
		ret = 1;
	return ret;

}
int main(int argc, char *argv[])
{
	char c;
	int i = 0;
	int count = 0;
	while ((c = getchar()) != '\n'){
		if (judge(c))
			count ++;
	}
	printf("%d\n", count);
	return 0;
}
