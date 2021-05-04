#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 10
#define NotFound 999
typedef int ElementType;

typedef int Position;
typedef struct LNode *List;
struct LNode {
    ElementType Data[MAXSIZE];
    Position Last; /* 保存线性表中最后一个元素的位置 */
};

List ReadInput(); /* 裁判实现，细节不表。元素从下标1开始存储 */
Position BinarySearch( List L, ElementType X );

int main()
{
    List L;
    ElementType X;
    Position P;

    L = ReadInput();
    scanf("%d", &X);
    P = BinarySearch( L, X );
    printf("%d\n", P);

    return 0;
}

/* 你的代码将被嵌在这里 */
List ReadInput(){
  List L = (List)malloc(sizeof(struct LNode));
  L->Last = -1;
  int n=0;
  scanf("%d", &n);
  for (int i=0; i<n; i++){
    scanf("%d", &L->Data[i]);
    L->Last++;
  }
  return L;
}
Position BinarySearch( List L, ElementType X ){
  int BinarySearch2(List L, Position left, Position right, ElementType X);
  int left=1;
  int right=L->Last;
  int ret = 0;
  ret = BinarySearch2(L, left, right, X);
  if (ret == -1) return NotFound;
  return ret;
}
int BinarySearch2(List L, Position left, Position right, ElementType X){
  if (left > right) return -1;
  int mid=(left+right)/2;
  if (L->Data[mid]==X) return mid;
  else if (L->Data[mid]>X) return BinarySearch2(L, left, mid-1, X);
  else return BinarySearch2(L, mid+1, right, X);
}
