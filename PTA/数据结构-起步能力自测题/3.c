#include <stdio.h>
#define MAXN 101

int a[MAXN] = {0};
void printAry(int n);
void f(int n, int move);
int main(void)
{
  int n, move;
  scanf("%d %d", &n, &move);
  for (int i = 0; i < n; i++){
    scanf("%d", &a[i]);
  }

  f(n, move);
  printAry(n);
  return 0;
}
void printAry(int n){
  for (int i = 0; i < n; i++){
    if (i != 0)
      printf(" ");
    printf("%d", a[i]);
  }
}
void f(int n, int move){
  int idxBegin = 0;
  int idx = idxBegin;
  int idxLast;
  int temp;
  int count = 0;
  while (count != n){
    temp = a[idx];

    do {
      idxLast = idx;
      idx -= move;
      while (idx < 0)
        idx += n;
      a[idxLast] = a[idx];
      count ++;
    }while (idx != idxBegin);
    a[idxLast] = temp;
    idxBegin++;
    idx = idxBegin;
  }
}
