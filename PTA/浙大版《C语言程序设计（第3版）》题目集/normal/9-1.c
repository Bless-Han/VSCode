#include <stdio.h>

int main(void)
{
	int hh, mm, ss;
	scanf("%d:%d:%d", &hh, &mm, &ss);
	int n;
	scanf("%d", &n);
	ss += n;
	for ( ; ss >= 60; ss -= 60, mm++) ;
	for ( ; mm >= 60; mm -= 60, hh++) ;
	for ( ; hh >= 24; hh -= 24) ;
	printf("%0.2d:%0.2d:%0.2d\n", hh, mm, ss);
	return 0;
}
