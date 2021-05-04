#include <stdio.h>
#define MAXN 20

void CountOff( int n, int m, int out[] );

int main()
{
    int out[MAXN], n, m;
    int i;

    scanf("%d %d", &n, &m);
    CountOff( n, m, out );   
    for ( i = 0; i < n; i++ )
        printf("%d ", out[i]);
    printf("\n");

    return 0;
}

/* 你的代码将被嵌在这里 */
void CountOff( int n, int m, int out[] )
{
	for (int i = 0; i < n; i++) {
		out[i] = 0;
	}
	int index = -1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			index++;
			if (index >= n) index -= n;
			while(out[index] != 0) {
				index ++;
				if (index >= n) index -= n;
			}
		}
		out[index] = i + 1;
	}
}
