#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char *argv[]){
	double n;
	scanf("%lf", &n);
	n /= 1000;
	double result = 0;
	double seven = 59.5 / 2;
	double oneToSix = 155.5 / 2 - seven;
	double once = oneToSix / 6;
	if (n <= 11.5 / 2)
		result = 10;
	else if (n <= 27.5 / 2)
		result = 9;
	else if (n <= 43.5 / 2)
		result = 8;
	else if (n <= 59.5 / 2)
		result = 7;
	else if(n <= 155.5 / 2){
		if (n <= seven + once * 1)
			result = 6;
		else if (n <= seven + once * 2)
			result = 5;
		else if (n <= seven + once * 3)
			result = 4;
		else if (n <= seven + once * 4)
			result = 3;
		else if (n <= seven + once * 5)
			result = 2;
		else if (n <= seven + once * 6)
			result = 1;
	}
	printf("%0.0lf\n", result);
	return 0;
}
