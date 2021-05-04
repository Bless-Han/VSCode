#include <stdio.h>

int main(void)
{
	int begin, end;
	scanf("%d %d", &begin, &end);
	int h, m;
	h = (end / 100) - (begin / 100);
	m = (end % 100) - (begin % 100);
	if (m < 0) {
		m += 60;
		h--;
	}
	printf("%0.2d:%0.2d\n", h, m);
	return 0;
}
