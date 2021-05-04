#include <stdio.h>
#define N 40

struct employe {
	char name[N + 1];
	double base;
	double floa;
	double out;
};
int main(int argc, char *argv[])
{
	int n;
	scanf("%d",&n);
	struct employe e[n];
	for (int i = 0; i < n; i++) {
		scanf("%s %lf %lf %lf", e[i].name, &e[i].base, &e[i].floa, &e[i].out);
	}
	for (int i = 0; i < n; i++) {
		printf("%s %0.2lf\n", e[i].name, e[i].base + e[i].floa - e[i].out);
	}
	return 0;
}
