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
	int n;
	struct ListNode *P = NULL;
	scanf("%d",&n);
	struct ListNode *Head;
	P = Head = (struct ListNode*)malloc(sizeof(struct ListNode));
	Head->data = n;
	Head->next = NULL;
	while (1) {
		scanf("%d",&n);
		if(n == -1) break;
		P->next = (struct ListNode*)malloc(sizeof(struct ListNode));
		P = P->next;
		P->data = n;
		P->next = NULL;
	}
	return Head;
}
struct ListNode *getodd( struct ListNode **L )
{
	struct ListNode *S_Head = NULL;  // Single head
	struct ListNode *Sin = NULL;  // Single number
	struct ListNode *D_Head = NULL;  // Double head
	struct ListNode *Dou = NULL;  // Double number
	struct ListNode *Temp = NULL;
	while (*L != NULL) {
		Temp = *L;
		if (((*L)->data)%2 != 0) {
			if (Sin == NULL) S_Head = Sin = (struct ListNode*)malloc(sizeof(struct ListNode));
			else {
				Sin->next = (struct ListNode*)malloc(sizeof(struct ListNode));
				Sin = Sin->next;
			}
			Sin->data = (*L)->data;
			Sin->next = NULL;
		} else {
			if (Dou == NULL) D_Head = Dou = (struct ListNode*)malloc(sizeof(struct ListNode));
			else {
				Dou->next = (struct ListNode*)malloc(sizeof(struct ListNode));
				Dou = Dou->next;
			}
			Dou->data = (*L)->data;
			Dou->next = NULL;
		}
		*L = (*L)->next;
		free(Temp);
	}
	*L = D_Head;
	return S_Head;
}
/*
习题11-7 奇数值结点链表 (20分)

本题要求实现两个函数，分别将读入的数据存储为单链表、将链表中奇数值的结点重新组成一个新的链表。链表结点定义如下：

struct ListNode {
    int data;
	    ListNode *next;
		};

		函数接口定义：

		struct ListNode *readlist();
		struct ListNode *getodd( struct ListNode **L );

		函数readlist从标准输入读入一系列正整数，按照读入顺序建立单链表。当读到−1时表示输入结束，函数应返回指向单链表头结点的指针。

		函数getodd将单链表L中奇数值的结点分离出来，重新组成一个新的链表。返回指向新链表头结点的指针，同时将L中存储的地址改为删除了奇数值结点后的链表的头结点地址（所以要传入L的指针）。
		裁判测试程序样例：


输入样例：

1 2 2 3 4 5 6 7 -1

输出样例：

1 3 5 7 
2 2 4 6 
*/
