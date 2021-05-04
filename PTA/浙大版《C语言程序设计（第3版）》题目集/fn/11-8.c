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
	struct ListNode *L = NULL;
	struct ListNode *Head = NULL;
	int n;
	scanf("%d", &n);
	while (n != -1) {
		if (L == NULL) L = Head = (struct ListNode*)malloc(sizeof(struct ListNode));
		else {
			L->next = (struct ListNode*)malloc(sizeof(struct ListNode));
			L = L->next;
		}
		L->data = n;
		L->next = NULL;
		scanf("%d", &n);
	}
	return Head;
}
struct ListNode *deletem( struct ListNode *L, int m )
{
	struct ListNode *P = NULL;
	struct ListNode *Head = NULL;
	struct ListNode *Temp = NULL;
	while (L) {
		if (L->data != m){
			if (P == NULL) P = Head = (struct ListNode*)malloc(sizeof(struct ListNode));
			else {
				P->next = (struct ListNode*)malloc(sizeof(struct ListNode));
				P = P->next;
			}
			P->data = L->data;
			P->next = NULL;
			L = L->next;
		} else {
			Temp = L;
			L = L->next;
			free(Temp);
		}
	}
	return Head;
}
