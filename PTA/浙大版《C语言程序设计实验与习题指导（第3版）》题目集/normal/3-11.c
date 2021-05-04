#include <stdio.h>

int main(void)
{
	int a, b;
	char c;
	scanf("%d %d %c", &a, &b, &c);
	double price = 0;
	switch (b) {
		case 90:price = 6.95; break;
		case 93:price = 7.44; break;
		case 97:price = 7.93; break;
	}
	double result = 0;
	if (c == 'm')
		result = a * price * 0.95;
	else if (c == 'e')
		result = a * price * 0.97;
	printf("%0.2lf\n", result);
	return 0;
}
