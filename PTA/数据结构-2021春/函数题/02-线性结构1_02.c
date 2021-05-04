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
  int n;
  scanf("%d", &n);
  List ret = (List)malloc(sizeof(struct Node));
  List last = ret;
  ret->Next = NULL;
  for (int i=0; i<n; i++){
    last->Next = (List)malloc(sizeof(struct Node));
    last=last->Next;
    scanf("%d", &last->Data);
  }
  last->Next = NULL;
  return ret;
} /* 细节在此不表 */
void Print( List L ){
  L=L->Next;
  if (L)
    for (; L; L=L->Next)
      printf("%d ", L->Data);
  else 
    printf("NULL");
  printf("\n");
} /* 细节在此不表；空链表将输出NULL */

List Merge( List L1, List L2 ){
  List l1=L1->Next;
  List l2=L2->Next;
  L1->Next = L2->Next = NULL;
  List ret = (List)malloc(sizeof(struct Node));
  List last = ret;
  ret->Next = NULL;
  while (l1 && l2){
    if (l1->Data < l2->Data) {
      last->Next = l1;
      l1 = l1->Next;
    } else {
      last->Next = l2;
      l2 = l2->Next;
    }
    last = last->Next;
  }
  for (; l1; l1=l1->Next){
    last->Next = l1;
    last = last->Next;
  }
  for (; l2; l2=l2->Next){
    last->Next = l2;
    last = last->Next;
  }
  last->Next = NULL;
  return ret;
}
