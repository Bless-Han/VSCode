#include <stdio.h>
#define MAX_N 17

struct person {
	char name[MAX_N + 1];
	int born;
	char number[MAX_N + 1];
};
void swap(struct person *m, int j);
int main(void)
{
	int n;
	scanf("%d", &n);
	struct person m[n];
	for (int i = 0; i < n; i++) scanf("%s%d%s", m[i].name, &m[i].born, m[i].number);
	for (int i = 0; i < n - 1; i++) {
		for (int j = n - 1; j > i; j--) {
			if (m[j].born < m[j - 1].born) swap( m, j);
		}
	}
	for (int i = 0; i < n; i++) printf("%s %d %s\n", m[i].name, m[i].born, m[i].number);
	return 0;
}
void swap(struct person *m, int j)
{
	struct person temp = m[j];
	m[j] = m[j - 1];
	m[j - 1] = temp;
}
