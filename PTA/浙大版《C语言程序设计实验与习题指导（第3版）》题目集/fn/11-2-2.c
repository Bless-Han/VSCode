#include <stdio.h>
#include <stdlib.h>

struct stud_node {
     int    num;
     char   name[20];
     int    score;
     struct stud_node *next;
};

struct stud_node *createlist();
struct stud_node *deletelist( struct stud_node *head, int min_score );

int main()
{
    int min_score;
    struct stud_node *p, *head = NULL;

    head = createlist();
    scanf("%d", &min_score);
    head = deletelist(head, min_score);
    for ( p = head; p != NULL; p = p->next )
        printf("%d %s %d\n", p->num, p->name, p->score);

    return 0;
}

/* 你的代码将被嵌在这里 */

struct stud_node *createlist()
{
	int number;
	scanf("%d",&number);
	struct stud_node *tail = NULL;
	struct stud_node *head = NULL;
	while (number != 0) {
		struct stud_node *q = (struct stud_node*)malloc(sizeof(struct stud_node));
		q->next = NULL;
		q->num = number;
		scanf("%s %d", q->name, &q->score);
		if (head == NULL)
			head = tail = q;
		else {
			tail->next = q;
			tail = tail->next;
		}
		scanf("%d",&number);
	}
	return head;
}
struct stud_node *deletelist( struct stud_node *head, int min_score )
{
	struct stud_node *temp = head;
	struct stud_node *tempLast = head;
	while (head != NULL && head->score < min_score) { // Delete object of front.
		temp = head;
		head = head->next;
		free(temp);
	}
	if (head != NULL){
		struct stud_node *tempLast = head;
		temp = head->next;
		while (temp != NULL) {
			if (temp->score < min_score){
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
