#include <stdio.h>
#include <math.h>
#define N 32

int change(char *s)
{
	int ret = 0;
	for (int i = 0; i < 8; i++) {
		ret += pow(2, 8 - i - 1) * (s[i] - '0');
	}
	return ret;
}
int main(int argc, char *argv[])
{
	char s[N + 1];
	scanf("%s", s);
	int ip[4];
	for (int i = 0; i < 4; i++) {
		ip[i] = change(&s[i * 8]);
	}
	printf("%d.%d.%d.%d\n", ip[0], ip[1], ip[2], ip[3]);
	return 0;
}
