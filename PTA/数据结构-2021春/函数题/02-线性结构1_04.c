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
  List ret = (List)malloc(sizeof(struct Node));
  ret->Next=NULL;
  List tmp = ret;
  int n;
  scanf("%d", &n);
  for(int i=0; i<n; i++){
    tmp->Next = (List)malloc(sizeof(struct Node));
    tmp=tmp->Next;
    scanf("%d", &tmp->Data);
  }
  tmp->Next=NULL;
  return ret;
}
void Print( List L ){
  L=L->Next;
  if (!L)
    puts("NULL");
  else{
    for( ; L; L=L->Next)
      printf("%d ", L->Data);
    printf("\n");
  }
}
List Merge( List L1, List L2 ){
  List ret = (List)malloc(sizeof(struct Node));
  ret->Next=NULL;
  List tmp = ret;
  List l1 = L1->Next;
  List l2 = L2->Next;
  L1->Next = L2->Next = NULL;
  for( ; l1 && l2; tmp=tmp->Next){
    if (l1->Data < l2->Data){
      tmp->Next = l1;
      l1=l1->Next;
    } else {
      tmp->Next = l2;
      l2=l2->Next;
    }
  }
  for( ; l1; tmp=tmp->Next) { tmp->Next = l1; l1=l1->Next; }
  for( ; l2; tmp=tmp->Next) { tmp->Next = l2; l2=l2->Next; }
  tmp->Next = NULL;
  return ret;
}
