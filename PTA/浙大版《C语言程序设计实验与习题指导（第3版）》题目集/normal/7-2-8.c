#include <stdio.h>
#define N 7

int judge(int a[N * N], int n, int x, int y)
{
	int ret = 1;
	for (int i = 0; i < n; i++) {
		if (x == i)
			continue;
		if (a[x * n + y] > a[i * n + y]){
			ret = 0;
			break;
		}
	}
	if (ret){
		for (int i = 0; i < n; i++) {
			if (y == i)
				continue;
			if (a[x * n + y] < a[x * n + i]){
				ret = 0;
				break;
			}
		}
	}
	return ret;
}
int main(int argc, char *argv[])
{
	int n;
	scanf("%d", &n);
	int x, y, flag;
	flag = x = y = 0;
	int a[N * N];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[i * n + j]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (judge(a, n, i, j)){
				flag = 1;
				x = i;
				y = j;
				break;
			}
		}
		if (flag)
			break;
	}
	if (flag) printf("%d %d\n", x, y);
	else puts("NONE");
	return 0;
}
