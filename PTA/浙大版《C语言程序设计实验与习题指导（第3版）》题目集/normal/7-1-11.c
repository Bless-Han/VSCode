#include <stdio.h>

struct times {
	int a[1000];
	int count[1000];
};
struct times add(struct times numbers, int i, int number)
{
	for (int j = 0; j < i; j++) {
		if (number == numbers.a[j]) {
			numbers.count[j]++;
			return numbers;
		}
	}
	numbers.count[i]++;
	return numbers;
}
int main(void)
{
	int n, number;
	struct times numbers;
	for (int i = 0; i < 1000; i++) 
		numbers.a[i] = numbers.count[i] = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &number);
		numbers = add(numbers, i, number);
		numbers.a[i] = number;
	}
	int max_index = 0;
	for (int i = 0; i < n; i++) {
		if (numbers.count[i] > numbers.count[max_index])
			max_index = i;
	}
	printf("%d %d\n", numbers.a[max_index], numbers.count[max_index]);
}
