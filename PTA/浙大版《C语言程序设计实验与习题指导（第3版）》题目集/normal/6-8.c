#include <stdio.h>

int main(void)
{
	char c;
	int sum, i;
	int number;
	int flag = 0;
	scanf("%d%c", &sum, &c);
	while (c != '=') {
		if (!(c == '+' || c == '-' || c == '*' || c == '/')){
			flag = 1;
			break;
		}
		scanf("%d", &number);
		if (c == '/' && number == 0){
			flag = 1;
			break;
		}
		switch (c) {
			case '+': sum += number; break; 
			case '-': sum -= number; break;
			case '*': sum *= number; break;
			case '/': sum /= number; break;
		}
		scanf("%c", &c);
	}
	if (flag) 
		printf("ERROR\n");
	else
		printf("%d\n", sum);
	return 0;
}
