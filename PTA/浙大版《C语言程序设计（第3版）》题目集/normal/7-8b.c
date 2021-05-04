#include <stdio.h>
#include <math.h>
#define MAX_N 500

int main(void)
{
	char a[MAX_N + 1];
	int i;
	for (i = 0; (a[i] = getchar()) != '#'; i++) ;
	a[i] = '\0';
	char b[MAX_N + 1];
	int index_b = 0;
	int flag = 0;
	for (int j = 0; j < i; j++) {
		if (a[j] == '-') if (flag == 0) flag = -1;
		if ((a[j] >= '0' && a[j] <= '9') || (a[j] >= 'a' && a[j] <= 'f') || (a[j] >= 'A' && a[j] <= 'F')) {
			if (flag == 0) flag = 1;
			b[index_b] = a[j];
			index_b++;
		}
	}
	index_b--;
	long long int result = 0;
	int temp;
	for (int j = 0; index_b >= 0; index_b--, j++) {
		if (b[index_b] >= '0' && b[index_b] <= '9') temp = b[index_b] - '0';
		else if (b[index_b] >= 'a' && b[index_b] <= 'f') temp = 10 + (b[index_b] - 'a');
		else if (b[index_b] >= 'A' && b[index_b] <= 'F') temp = 10 + (b[index_b] - 'A');
		result += temp * pow(16, j);
	}
	printf("%d\n", result * flag);
	return 0;
}
