#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char *argv[]){
	int n;
	scanf("%d", &n);
	int a, b, c;
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &a, &b, &c);
		if (pow(a, 2) + pow(b, 2) + pow(c, 2) == 3 * a * b * c)
			puts("Yes");
		else
			puts("No");
	}
	return 0;
}
