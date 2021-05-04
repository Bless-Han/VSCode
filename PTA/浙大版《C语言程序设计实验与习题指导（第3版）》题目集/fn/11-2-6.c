#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *readlist();
struct ListNode *getodd( struct ListNode **L );
void printlist( struct ListNode *L )
{
     struct ListNode *p = L;
     while (p) {
           printf("%d ", p->data);
           p = p->next;
     }
     printf("\n");
}

int main()
{
    struct ListNode *L, *Odd;
    L = readlist();
    Odd = getodd(&L);
    printlist(Odd);
    printlist(L);

    return 0;
}

/* 你的代码将被嵌在这里 */

struct ListNode *readlist()
{
	struct ListNode *head = NULL;
	struct ListNode *tail = NULL;
	int number;
	scanf("%d", &number);
	while (number != -1) {
		struct ListNode *p = (struct ListNode*)malloc(sizeof(struct ListNode));
		p->next = NULL;
		p->data = number;
		if (head == NULL)
			head = tail = p;
		else
			tail = tail->next = p;
		scanf("%d", &number);
	}
	return head;
}
struct ListNode *getodd( struct ListNode **L )
{
	struct ListNode *p = *L;
	struct ListNode *singleHead = NULL;
	struct ListNode *singleTail = NULL;
	struct ListNode *doubleHead = NULL;
	struct ListNode *doubleTail = NULL;
	while (p != NULL) {
		if (p->data % 2 == 1){
			if (singleHead == NULL){
				singleHead = singleTail = p;
				p = p->next;
				singleTail->next = NULL;
			} else {
				singleTail = singleTail->next = p;
				p = p->next;
				singleTail->next = NULL;
			}
		} else {
			if (doubleHead == NULL){
				doubleHead = doubleTail = p;
				p = p->next;
				doubleTail->next = NULL;
			} else {
				doubleTail = doubleTail->next = p;
				p = p->next;
				doubleTail->next = NULL;
			}
		}
	}
	*L = doubleHead;
	return singleHead;
}
