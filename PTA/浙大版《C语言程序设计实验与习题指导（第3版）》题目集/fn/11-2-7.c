#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    char code[8];
    struct ListNode *next;
};

struct ListNode *createlist() /*裁判实现，细节不表*/
{
	struct ListNode *head = NULL;
	struct ListNode *tail = NULL;
	char s[8];
	scanf("%s", s);
	while (s[0] != '#') {
		struct ListNode *p = (struct ListNode*)malloc(sizeof(struct ListNode));
		p->next = NULL;
		strcpy(p->code, s);
		if (head == NULL)
			head = tail = p;
		else
			tail = tail->next = p;
		scanf("%s", s);
	}
	return head;
}
int countcs( struct ListNode *head );

int main()
{
    struct ListNode  *head;

    head = createlist();
    printf("%d\n", countcs(head));

    return 0;
}

/* 你的代码将被嵌在这里 */
int countcs( struct ListNode *head )
{
	int ret = 0;
	while (head != NULL) {
		if (head->code[1] == '0' && head->code[2] == '2')
			ret++;
		head = head->next;
	}
	return ret;
}
