#include <stdio.h>

int main(void)
{
	char c;
	int a;
	int sum;
	scanf("%d", &sum);
	while ((c = getchar()) != '=') {
		switch (c) {
			case '/': 
				scanf("%d", &a);
				if (a == 0) {
					printf("ERROR\n");
					goto END;
				} else sum /= a;
				break;
			case '+': scanf("%d", &a); sum += a; break;
			case '-': scanf("%d", &a); sum -= a; break;
			case '*': scanf("%d", &a); sum *= a; break;
			default: 
					  printf("ERROR\n");
					  goto END;
				
		}
	}
	printf("%d\n", sum);
END:
	return 0;
}
