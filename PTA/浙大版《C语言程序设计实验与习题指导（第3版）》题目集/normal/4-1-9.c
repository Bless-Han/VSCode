#include <stdio.h>

int main(void)
{
	int random, n;
	scanf("%d %d", &random, &n);
	int guess;
	int i;
	for (i = 0; i < n; i++) {
		scanf("%d", &guess);
		if (guess == random || guess < 0)
			break;
		else if (guess > random) printf("Too big\n");
		else if (guess < random) printf("Too small\n");
	}
	if (i + 1 == 1 && guess >= 0) 
		printf("Bingo!\n");
	else if (i + 1 == 2 || i + 1 == 3 && guess >= 0) 
		printf("Lucky You!\n");
	else if (i + 1 <= n && guess >= 0) 
		printf("Good Guess!\n");
	else 
		printf("Game Over\n");
	return 0;
}
