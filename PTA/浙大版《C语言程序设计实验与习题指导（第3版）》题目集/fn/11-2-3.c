#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *createlist();

int main()
{
    struct ListNode *p, *head = NULL;

    head = createlist();
    for ( p = head; p != NULL; p = p->next )
        printf("%d ", p->data);
    printf("\n");

    return 0;
}

/* 你的代码将被嵌在这里 */

struct ListNode *createlist()
{
	int number;
	struct ListNode *head = NULL;
	scanf("%d", &number);
	while (number != -1) {
		struct ListNode *p = (struct ListNode*)malloc(sizeof(struct ListNode));
		p->data = number;
		if (head == NULL){
			p->next = NULL;
			head = p;
		} else {
			p->next = head;
			head = p;
		}
		scanf("%d", &number);
	}
	return head;
}
