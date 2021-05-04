#include <stdio.h>
#define MAX_N 10000

struct goods{
	int a[MAX_N];
	int boxes[MAX_N];
	int a_index[MAX_N];
};
int main(int argc, char *argv[])
{
	struct goods a;
	for (int i = 0; i < MAX_N; i++) {
		a.a[i] = a.boxes[i] = a.a_index[i] = 0;
	}
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a.a[i]);
		for (int j = 0; j < n; j++) {
			if (a.a[i] + a.boxes[j] <= 100){
				a.boxes[j] += a.a[i];
				a.a_index[i] = j;
				break;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d %d\n", a.a[i], a.a_index[i] + 1);
	}
	int i;
	for (i = 0; a.boxes[i] != 0; i++) ;
	printf("%d\n", i);
	return 0;
}
