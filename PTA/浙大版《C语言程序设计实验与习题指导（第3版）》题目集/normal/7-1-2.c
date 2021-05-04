#include <stdio.h>
#define MAX_N 10

int main(void)
{
	int n;
	scanf("%d", &n);
	int a[MAX_N];
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	int index, max;
	for (int i = 0; i < n; i++) {
		if (i == 0){
			index = i;
			max = a[i];
		}
		if (a[i] > max){
			max = a[i];
			index = i;
		}
	}
	printf("%d %d\n", max, index);
	return 0;
}
