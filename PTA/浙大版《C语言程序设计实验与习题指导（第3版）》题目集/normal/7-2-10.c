#include <stdio.h>
#define N 15

void pr(char a[], int n)
{
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (j) printf(" ");
			printf("%c", a[i * n + j]);
		}
		printf("\n");
	}
}
int judge(char a[], int x1, int y1, int x2, int y2, int n)
{
	int ret = 1;
	if (a[x1 * n + y1] == a[x2 * n + y2] && (a[x1 * n + y1] != '*' && a[x2 * n + y2] != '*')){
		a[x1 * n + y1] = '*';
		a[x2 * n + y2] = '*';
	}
	else
		ret = 0;
	return ret;
}
int congra(char a[], int n)
{
	int ret = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (a[i * n + j] != '*'){
				ret = 0;
				break;
			}
		}
	}
	return ret;
}

int main(int argc, char *argv[])
{
	char a[N * N] = {0};
	int n;
	scanf("%d\n", &n);
	n *= 2;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%c ", &a[i * n + j]);
		}
	}
	int k, x1, y1, x2, y2;
	int error = 0;
	scanf("%d", &k);
	for (int i = 0; i < k; i++) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		x1--; y1--; x2--; y2--;
		if (judge(a, x1, y1, x2, y2, n)){
			if (congra(a, n)){
				printf("Congratulations!\n");
				break;
			}
			pr(a, n);
		} else {
			printf("Uh-oh\n");
			error++;
		}
		if (error == 3){
			printf("Game Over\n");
			break;
		}
	}
	return 0;
}
