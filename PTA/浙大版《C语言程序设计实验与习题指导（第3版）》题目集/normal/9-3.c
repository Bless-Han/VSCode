#include <stdio.h>
#define N 10

struct pupils {
	int number;
	char name[N + 1];
	int mark;
};
int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);
	struct pupils p[n];
	int sum = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d %s %d", &p[i].number, p[i].name, &p[i].mark);
		sum += p[i].mark;
	}
	double average = sum / n;
	printf("%0.2lf\n", average);
	for (int i = 0; i < n; i++) {
		if (p[i].mark < average)
			printf("%s %0.5d\n", p[i].name, p[i].number);
	}
	return 0;
}
