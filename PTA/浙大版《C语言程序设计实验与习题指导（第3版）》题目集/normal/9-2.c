#include <stdio.h>

int main(int argc, char *argv[])
{
	int hh, mm, ss, n;
	scanf("%d:%d:%d", &hh, &mm, &ss);
	scanf("%d", &n);
	ss += n;
	if (ss >= 60){
		ss -= 60;
		mm++;
	}
	if (mm >= 60){
		mm -= 60;
		hh ++;
	}
	if (hh >= 24){
		hh -= 24;
	}
	printf("%0.2d:%0.2d:%0.2d\n", hh, mm, ss);
	return 0;
}
