#include <stdio.h>
#include <string.h>
#define MAX_N 80
#define N 5

int main(void)
{
	char a[N][MAX_N + 1];
	for (int i = 0; i < N; i++) scanf("%s", a[i]);
	int index[N];
	for (int i = 0; i < N; i++) index[i] = 1;
	char b[N][MAX_N + 1];
	char temp[MAX_N + 1];
	int flag;
	int least;
	for (int i = 0; i < N; i++) {
		for (int j = 0, flag = 1; j < N; j++) {
			if (index[j] == 0) continue;
			else if (index[j] == 1 && flag == 1) {
				flag = 0;
				least = j;
			}
			if (strcmp(a[least], a[j]) > 0 && least != j) {
				least = j;
			}
		}
		index[least] = 0;
		strcpy(b[i], a[least]);
	}
	printf("After sorted:\n");
	for (int i = 0; i < N; i++) printf("%s\n", b[i]);
	return 0;
}
