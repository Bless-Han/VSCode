#include <stdio.h>

int main(void)
{
	int year, month, day;
	scanf("%d/%d/%d", &year, &month, &day);
	int sum = 0;
	switch (month) {
		case 11 + 1: sum += 30;
		case 10 + 1: sum += 31;
		case 9 + 1: sum += 30;
		case 8 + 1: sum += 31;
		case 7 + 1: sum += 31;
		case 6 + 1: sum += 30;
		case 5 + 1: sum += 31;
		case 4 + 1: sum += 30;
		case 3 + 1: sum += 31;
		case 2 + 1: sum += 28;
				 if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) sum += 1;
		case 1 + 1: sum += 31;
		default: sum += day;
	}
	printf("%d\n", sum);
	return 0;
}
