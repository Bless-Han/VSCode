#include <stdio.h>

int main(void)
{
	int t;
	scanf("%d", &t);
	int a[t];
	for (int i = 0; i < t; i++) a[i] = 0;
	int n , temp;
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				scanf("%d", &temp);
				if (x < y && temp != 0) a[i] = -1;
			}
		}
	}
	for (int i = 0; i < t; i++) {
		if (a[i] == -1) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}
