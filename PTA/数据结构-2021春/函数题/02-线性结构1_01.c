#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data;
    PtrToNode   Next;
};
typedef PtrToNode List;

List Read(); /* 细节在此不表 */
void Print( List L ); /* 细节在此不表；空链表将输出NULL */

List Merge( List L1, List L2 );

int main()
{
    List L1, L2, L;
    L1 = Read();
    L2 = Read();
    L = Merge(L1, L2);
    Print(L);
    Print(L1);
    Print(L2);
    return 0;
}

/* 你的代码将被嵌在这里 */
List Read(){
  int n=0;
  List ret = (List)malloc(sizeof(PtrToNode));
  ret->Next = NULL;
  List r = ret;
  scanf("%d", &n);
  for (int i=0; i<n; i++){
    List p = (List)malloc(sizeof(struct Node));
    scanf("%d", &(p->Data));
    r->Next = p;
    r = p;
    r->Next = NULL;
  }
  return ret;
}
void Print( List L ){
  List t = L->Next;
  if (t){
    while(t){
      printf("%d ", t->Data);
      // t = t->Next;
    }
    printf("\n");
  } else {
    printf("NULL\n");
  }
}

List Merge( List L1, List L2 ){
  List ret = (List)malloc(sizeof(PtrToNode));
  List l1 = L1->Next;
  List l2 = L2->Next;
  ret->Next = NULL;
  List temp = ret;
  while (l1 && l2){
    if (l1->Data < l2->Data){
      temp->Next = l1;
      l1 = l1->Next;
    } else {
      temp->Next = l2;
      l2 = l2->Next;
    }
    temp = temp->Next;
  }
  while (l1){
    temp->Next = l1;
    temp = temp->Next;
    l1 = l1->Next;
  }
  while (l2){
    temp->Next = l2;
    l2 = l2->Next;
    temp = temp->Next;
  }
  L1->Next = L2->Next = temp->Next = NULL;
  return ret;
}
