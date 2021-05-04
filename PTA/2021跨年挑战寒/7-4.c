#include <stdio.h>
#include <string.h>
#include <math.h>

void f(int a, int b){
	if ((a == 1 && b == 2) || (a ==2 && b == 1))
		printf("1 ke 2\n");
	else if ((a == 1 && b == 3) || (a ==3 && b == 1))
		printf("1 sheng 3\n");
	else if ((a == 1 && b == 4) || (a ==4 && b == 1))
		printf("4 ke 1\n");
	else if ((a == 1 && b == 5) || (a ==5 && b == 1))
		printf("5 sheng 1\n");
	else if ((a == 2 && b == 3) || (a ==3 && b == 2))
		printf("3 sheng 2\n");
	else if ((a == 2 && b == 4) || (a ==4 && b == 2))
		printf("2 sheng 4\n");
	else if ((a == 2 && b == 5) || (a ==5 && b == 2))
		printf("2 ke 5\n");
	else if ((a == 3 && b == 4) || (a ==4 && b == 3))
		printf("3 ke 4\n");
	else if ((a == 3 && b == 5) || (a ==5 && b == 3))
		printf("5 ke 3\n");
	else if ((a == 4 && b == 5) || (a ==5 && b == 4))
		printf("4 sheng 5\n");

}
int main(int argc, char *argv[]){
	int n;
	scanf("%d", &n);
	int a, b;
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &a, &b);
		f(a, b);
	}
	return 0;
}
