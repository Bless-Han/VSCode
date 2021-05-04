#include <stdio.h>
#define MAXS 15

void StringCount( char *s );
void ReadString( char *s ); /* 由裁判实现，略去不表 */

int main()
{
    char s[MAXS];

    ReadString(s);
    StringCount(s);

    return 0;
}

/* Your function will be put here */

void StringCount( char *s )
{
	int big, little, space, number, other;
	big = little = space = number = other = 0;
	int n = 0;
	while (s[n] != '\0') {
		if (s[n] >= 'A' && s[n] <= 'Z') big ++;
		else if (s[n] >= 'a' && s[n] <= 'z') little ++;
		else if (s[n] >= '0' && s[n] <= '9') number ++;
		else if (s[n] == ' ') space ++;
		else other ++;
		n++;
	}
	printf("%d %d %d %d %d\n",big, little, space, number, other);
}
void ReadString( char *s ) /* 由裁判实现，略去不表 */
{
	int i = 0;
	while ((s[i] = getchar()) != '\n') i++;
	s[i] = '\0';
}
