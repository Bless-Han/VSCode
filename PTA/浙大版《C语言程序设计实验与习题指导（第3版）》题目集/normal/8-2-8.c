#include <stdio.h>
#include <string.h>
#define N 80

void swap(char s[5][N + 1], int i, int j)
{
	char temp[N + 1];
	strcpy(temp, s[i]);
	strcpy(s[i], s[j]);
	strcpy(s[j], temp);
}
void sort(char s[5][N + 1])
{
	for (int i = 0; i < 5 - 1; i++) {
		for (int j = 0; j < 5 - 1 - i; j++) {
			if (strcmp(s[j], s[j + 1]) > 0)
				swap(s, j, j + 1);
		}
	}
}
int main(int argc, char *argv[])
{
	char s[5][N + 1];
	for (int i = 0; i < 5; i++) {
		scanf("%s", s[i]);
	}
	sort(s);
	printf("After sorted:\n");
	for (int i = 0; i < 5; i++) {
		printf("%s\n", s[i]);
	}
	return 0;
}
