#include <stdio.h>

int main(void)
{
	int a, b, c, d, e;
	a = b = c = d = e = 0;
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int temp;
		scanf("%d", &temp);
		if (temp >= 90) a++;
		else if (temp >= 80) b++;
		else if (temp >= 70) c++;
		else if (temp >= 60) d++;
		else e++;
	}
	printf("%d %d %d %d %d\n", a, b, c, d, e);
	return 0;
}
