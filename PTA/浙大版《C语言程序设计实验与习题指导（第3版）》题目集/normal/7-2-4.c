#include <stdio.h>

int main(int argc, char *argv[])
{
	int y, m, d;
	scanf("%d/%d/%d", &y, &m, &d);
	int days = 0;
	days += d;
	switch (m - 1){
		case 12:days += 31;
		case 11:days += 30;
		case 10:days += 31;
		case 9:days += 30;
		case 8:days += 31;
		case 7:days += 31;
		case 6:days += 30;
		case 5:days += 31;
		case 4:days += 30;
		case 3:days += 31;
		case 2:days += 28;
		case 1:days += 31;
	}
	if (((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) && (m > 2))
		days++;
	printf("%d\n", days);
	return 0;
}
