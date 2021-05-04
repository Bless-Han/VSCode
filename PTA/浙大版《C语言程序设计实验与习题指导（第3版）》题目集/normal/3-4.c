#include <stdio.h>
#define N 10

int main(void)
{
	int letter, blank, digit, other;
	letter = blank = digit = other = 0;
	for (int i = 0; i < N; i++) {
		char c;
		c = getchar();
		if ((c >= 'a' && c <='z') || (c >= 'A' && c <= 'Z')) letter++;
		else if (c == ' ' || c == '\n') blank++;
		else if (c >= '0' && c <= '9') digit++;
		else other++;
	}
	printf("letter = %d, blank = %d, digit = %d, other = %d\n", letter, blank, digit, other);
	return 0;
}
