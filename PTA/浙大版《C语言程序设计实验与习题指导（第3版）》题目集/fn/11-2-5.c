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
struct ListNode *mergelists(struct ListNode *list1, struct ListNode *list2);
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
    struct ListNode  *list1, *list2;

    list1 = createlist();
    list2 = createlist();
    list1 = mergelists(list1, list2);
    printlist(list1);

    return 0;
}

/* 你的代码将被嵌在这里 */

struct ListNode *mergelists(struct ListNode *list1, struct ListNode *list2)
{
	struct ListNode *head = NULL;
	struct ListNode *tail = NULL;
	while (list1 != NULL && list2 != NULL) {
		if (list1->data <= list2->data) {
			if (head == NULL) {
				head = tail = list1;
				list1 = list1->next;
				tail->next = NULL;
			} else {
				tail = tail->next = list1;
				list1 = list1->next;
				tail->next = NULL;
			}
		} else {
			if (head == NULL) {
				head = tail = list2;
				list2 = list2->next;
				tail->next = NULL;
			} else {
				tail = tail->next = list2;
				list2 = list2->next;
				tail->next = NULL;
			}
		}
	}
	while (list1 != NULL) {
		if (head == NULL) {
			head = tail = list1;
			list1 = list1->next;
			tail->next = NULL;
		} else {
			tail = tail->next = list1;
			list1 = list1->next;
			tail->next = NULL;
		}
	}
	while (list2 != NULL) {
		if (head == NULL) {
			head = tail = list2;
			list2 = list2->next;
			tail->next = NULL;
		} else {
			tail = tail->next = list2;
			list2 = list2->next;
			tail->next = NULL;
		}
	}
	return head;
}
