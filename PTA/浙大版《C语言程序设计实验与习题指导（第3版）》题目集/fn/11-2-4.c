#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *createlist();
struct ListNode *deleteeven( struct ListNode *head );
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
    struct ListNode *head;

    head = createlist();
    head = deleteeven(head);
    printlist(head);

    return 0;
}

/* 你的代码将被嵌在这里 */
struct ListNode *createlist()
{
	int number;
	scanf("%d", &number);
	struct ListNode *head = NULL;
	struct ListNode *tail = NULL;
	while (number != -1) {
		struct ListNode *p = (struct ListNode*)malloc(sizeof(struct ListNode));
		p->next = NULL;
		p->data = number;
		if (head == NULL) {
			head = tail = p;
		} else {
			tail->next = p;
			tail = tail->next;
		}
		scanf("%d", &number);
	}
	return head;
}
struct ListNode *deleteeven( struct ListNode *head )
{
	struct ListNode *temp = NULL;
	while (head != NULL && head->data % 2 == 0) { // First delete the all object of front
		temp = head;
		head = head->next;
		free(temp);
	}
	if (head != NULL){
		struct ListNode *tempLast = head;
		temp = head->next;
		while (temp != NULL) {
			if (temp->data % 2 == 0){
				temp = temp->next;
				free(tempLast->next);
				tempLast->next = temp;
			} else {
				temp = temp->next;
				tempLast = tempLast->next;
			}
		}
	}
	return head;
}
