#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *readlist();
struct ListNode *deletem( struct ListNode *L, int m );
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
    int m;
    struct ListNode *L = readlist();
    scanf("%d", &m);
    L = deletem(L, m);
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
struct ListNode *deletem( struct ListNode *L, int m )
{
	struct ListNode *head = NULL;
	struct ListNode *tail = NULL;
	while (L != NULL) {
		if (L-> data != m){
			if (head == NULL) {
				head = tail = L;
				L = L->next;
				tail->next = NULL;
			}
			else {
				tail = tail->next = L;
				L = L->next;
				tail->next = NULL;
			}
		} else {
			L = L->next;
		}
	}
	return head;
}
