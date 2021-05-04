#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct stud_node {
     int    num;
     char   name[20];
     int    score;
     struct stud_node *next;
};
struct stud_node *head, *tail;

void input();

int main()
{
    struct stud_node *p;

    head = tail = NULL;
    input();
    for ( p = head; p != NULL; p = p->next )
        printf("%d %s %d\n", p->num, p->name, p->score);

    return 0;
}

/* 你的代码将被嵌在这里 */
void input()
{
	int number;
	scanf("%d", &number);
	while (number != 0) {
		struct stud_node *q = (struct stud_node*)malloc(sizeof(struct stud_node)); 
		q->next = NULL;
		q->num = number;
		scanf("%s %d", q->name, &(q->score));
		if (head == NULL)
			head = tail = q;
		else {
			tail->next = q;
			tail = tail->next;
		}
		scanf("%d", &number);
	}
}
