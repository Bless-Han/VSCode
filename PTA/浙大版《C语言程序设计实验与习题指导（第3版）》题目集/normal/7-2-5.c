#include <stdio.h>

int main(int argc, char *argv[])
{
	int t;
	scanf("%d", &t);
	int n, flag;
	int a[10][10];
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		flag = 1;
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				scanf("%d", &a[j][k]);
			}
		}
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < j; k++) {
				if (a[j][k] != 0){
					flag = 0;
					break;
				}
			}
			if (!flag)
				break;
		}
		if (flag) puts("YES");
		else puts("NO");
	}
	return 0;
}

// n = 3
// 0,0    0,1    0,2
// 1,0    1,1    1,2
// 2,0    2,1    2,2
