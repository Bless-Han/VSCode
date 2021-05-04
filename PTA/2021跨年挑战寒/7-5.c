#include <stdio.h>
#include <string.h>
#include <math.h>

double fact(double n){
	double ret = 1;
	for (double i = 1; i <= n; i++) {
		ret *= i;
	}
	return ret;
}
int main(int argc, char *argv[]){
	double a, b;
	scanf("%d %d", &a, &b);
	double flag = 0;
	double temp;
	double temp2;
	for ( ; a <= b; a++) {
		temp = a * a + 1;
		temp2 = fact(a); 
		printf("temp = %d\n", a * a);
		if (temp / temp2 - 1 == 0){
			flag = 1;
			printf("%d\n", a);
		}
	}
	if (!flag)
		puts("None");
	return 0;
}
