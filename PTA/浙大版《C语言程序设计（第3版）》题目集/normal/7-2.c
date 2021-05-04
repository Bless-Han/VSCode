#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int temp, max, index;
	for (int i = 0; i < n; i++) {
		scanf("%d", &temp);
		if (i == 0) {
			max = temp;
			index = i;
		} else {
			if (max < temp) {
				max = temp;
				index = i;
			}
		}
	}
	printf("%d %d\n", max, index);
	return 0;
}

