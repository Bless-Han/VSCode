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
  scanf("%d", &n);
  List ret = (List)malloc(sizeof(PtrToNode));
  ret->Next = NULL;
  List temp = ret;
  for (int i=0; i<n; i++){
    temp->Next = (List)malloc(sizeof(PtrToNode));
    temp = temp->Next;
    temp->Next = NULL;
    scanf("%d", &(temp->Data));
  }
  return ret;
}
void Print( List L ){
  if (!L->Next)
    printf("NULL\n");
  else {
    while(L->Next) {
      printf("%d ", L->Next->Data);
      L = L->Next;
    }
    printf("\n");
  }
}

List Merge( List L1, List L2 ){
  List l1 = L1->Next;
  List l2 = L2->Next;
  L1->Next = L2->Next = NULL;
  List ret = (List)malloc(sizeof(PtrToNode));
  List temp = ret;
  while (l1 && l2) {
    if (l1->Data < l2->Data){
      temp->Next = l1;
      l1 = l1->Next;
    } else {
      temp->Next = l2;
      l2 = l2->Next;
    }
    temp = temp->Next;
  }
  while (l1) {
      temp->Next = l1;
      l1 = l1->Next;
      temp = temp->Next;
  }
  while (l2) {
      temp->Next = l2;
      l2 = l2->Next;
      temp = temp->Next;
  }
  temp->Next = NULL;
  return ret;
}
