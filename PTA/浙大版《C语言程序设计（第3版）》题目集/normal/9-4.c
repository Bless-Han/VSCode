#include <stdio.h>
#define MAX_N 30

struct Book {
	char s[MAX_N + 1];
	double price;
};
int main(void)
{
	int n;
	scanf("%d", &n);
	getchar();
	struct Book m[n];
	int max, min;
	for (int i = 0; i < n; i++) {
		int j;
		for (j = 0; (m[i].s[j] = getchar()) != '\n'; j++) ;
		m[i].s[j] = '\0';
		scanf("%lf", &m[i].price);
		getchar();
		if (i == 0) {
			min = i;
			max = i;
		} else {
			if (m[min].price > m[i].price) min = i;
			if (m[max].price < m[i].price) max = i;
		}
	}
	printf("%0.2lf, %s\n", m[max].price, m[max].s);
	printf("%0.2lf, %s\n", m[min].price, m[min].s);
	return 0;
}
