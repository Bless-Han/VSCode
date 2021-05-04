#include <stdio.h>

void pr(int numbers[10])
{
	for (int i = 1; i < 10; i++) {
		if (numbers[i]){
			printf("%d", i);
			numbers[i]--;
			break;
		}
	}
	for (int i = 0; i < 10; i++) {
		while (numbers[i]){
			printf("%d", i);
			numbers[i]--;
		}
	}
}
int main(void)
{
	int numbers[10] = {0};
	for (int i = 0; i < 10; i++) {
		scanf("%d", &numbers[i]);
	}
	pr(numbers);
	printf("\n");
	return 0;
}
