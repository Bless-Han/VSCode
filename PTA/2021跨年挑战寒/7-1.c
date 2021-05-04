#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char *argv[]){
	int number;
	int sum = 0;
	for (int i = 0; i < 4; i++) {
		scanf("%d", &number);
		sum += number;
	}
	printf("%d\n", sum);
	return 0;
}
