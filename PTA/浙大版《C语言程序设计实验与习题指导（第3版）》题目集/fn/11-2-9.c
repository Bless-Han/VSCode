#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *createlist() /*裁判实现，细节不表*/
{
	struct ListNode *head = NULL;
	struct ListNode *tail = NULL;
	int number;
	scanf("%d", &number);
	while (number != -1) {
		struct ListNode *p = (struct ListNode*)malloc(sizeof(struct ListNode));
		p->data = number;
		p->next = NULL;
		if (head == NULL)
			head = tail = p;
		else 
			tail = tail->next = p;
		scanf("%d", &number);
	}
	return head;
}
struct ListNode *reverse( struct ListNode *head );
void printlist( struct ListNode *head )
{
     struct ListNode *p = head;
     while (p) {
           printf("%d ", p->data);
           p = p->next;
     }
     printf("\n");
}

int main()
{
    struct ListNode  *head;

    head = createlist();
    head = reverse(head);
    printlist(head);

    return 0;
}

/* 你的代码将被嵌在这里 */

struct ListNode *reverse( struct ListNode *head )
{
	struct ListNode *newHead = NULL;
	struct ListNode *newLast = NULL;
	while (head != NULL) {
		if (newHead == NULL) {
			newHead = newLast = head;
			head = head->next;
			newLast->next = NULL;
		} else {
			newHead = head;
			head = head->next;
			newHead->next = newLast;
			newLast = newHead;
		}
	}
	return newHead;
}
