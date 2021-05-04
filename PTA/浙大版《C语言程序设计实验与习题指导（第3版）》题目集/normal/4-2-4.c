#include <stdio.h>

int main(void)
{
	int count = 0;
	int x;
	scanf("%d", &x);
	for (int wu = x; wu > 0; wu--) {
		for (int er = x; er > 0; er--) {
			for (int yi = x; yi > 0; yi--) {
				if (wu * 5 + er * 2 + yi == x){
					printf("fen5:%d, fen2:%d, fen1:%d, total:%d\n", wu, er, yi, wu + er + yi);
					count ++;
				}
			}
		}
	}
	printf("count = %d\n", count);
	return 0;
}
