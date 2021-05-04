#include <stdio.h>
#include <stdlib.h>

typedef struct PolyNode *Polynomial;
struct PolyNode{
  int coef;
  int expon;
  Polynomial link;
};
Polynomial ReadPoly();
Polynomial PolyAdd(Polynomial P1, Polynomial P2);
Polynomial Mult(Polynomial P1, Polynomial P2);
void PrintPoly(Polynomial P);
int Compare(int a, int b);
void Attach(int c, int e, Polynomial *pRear);
int main(){
  Polynomial P1, P2, PP, PS;

  P1 = ReadPoly ();
  P2 = ReadPoly ();
  PP = Mult( P1, P2);
  PrintPoly(PP);
  PS = PolyAdd(P1, P2);
  PrintPoly(PS);
  return 0;
}
Polynomial ReadPoly(){
  Polynomial P = (Polynomial)malloc(sizeof(struct PolyNode));
  P->link = NULL;
  Polynomial Rear = P;
  int c, e;
  int n=0;
  scanf("%d", &n);
  for (int i=0; i<n; i++){
    scanf("%d %d", &c, &e);
    Attach(c, e, &Rear);
  }
  Rear = P;
  P = P->link;
  free(Rear);
  return P;
}
Polynomial PolyAdd(Polynomial P1, Polynomial P2){
  Polynomial front, rear, temp;
  int sum;
  rear = (Polynomial)malloc(sizeof(struct PolyNode));
  front = rear;
  while (P1 && P2)
    switch(Compare(P1->expon, P2->expon)){
      case 1:
        Attach(P1->coef, P1->expon, &rear);
        P1 = P1->link;
        break;
      case -1:
        Attach(P2->coef, P2->expon, &rear);
        P2 = P2->link;
        break;
      case 0:
        sum = P1->coef + P2->coef;
        if (sum) Attach(sum, P1->expon, &rear);
        P1 = P1->link;
        P2 = P2->link;
        break;
    }
  for (; P1; P1 = P1->link) Attach(P1->coef, P1->expon, &rear);
  for (; P2; P2 = P2->link) Attach(P2->coef, P2->expon, &rear);
  rear->link = NULL;
  temp = front;
  front = front->link;
  free(temp);
  return front;
}
Polynomial Mult(Polynomial P1, Polynomial P2){
  Polynomial P, Rear, t1, t2, t;
  int c, e;
  if (!P1 || !P2) return NULL;

  t1 = P1; t2 = P2;
  P = (Polynomial)malloc(sizeof(struct PolyNode)); P->link = NULL;
  Rear = P;
  while(t2){
    Attach(t1->coef*t2->coef, t1->expon+t2->expon, &Rear);
    t2 = t2->link;
  }
  t1 = t1->link;
  while(t1){
    t2 = P2; Rear = P;
    while(t2){
      c = t1->coef * t2->coef;
      e = t1->expon + t2->expon;
      while(Rear->link && Rear->link->expon > e)
        Rear = Rear->link;
      if (Rear->link && Rear->link->expon == e){
        if (Rear->link->coef + c)
          Rear->link->coef += c;
        else {
          t = Rear->link;
          Rear->link = t->link;
          free(t);
        }
      }
      else {
        t = (Polynomial)malloc(sizeof(struct PolyNode));
        t->coef = c; t->expon = e;
        t->link = Rear->link;
        Rear->link = t; Rear = Rear->link;
      }
      t2 = t2->link;
    }
    t1 = t1->link;
  }
  t2 = P; P = P->link; free(t2);

  return P;
}
int Compare(int a, int b){
  int ret = 0;
  if (a > b)
    ret = 1;
  else if (a < b)
    ret = -1;
  return ret;
}
void Attach(int c, int e, Polynomial *pRear){
  Polynomial P;

  P=(Polynomial)malloc(sizeof(struct PolyNode));
  P->coef = c;
  P->expon = e;
  P->link = NULL;
  (*pRear)->link = P;
  *pRear = P;
}
void PrintPoly(Polynomial P){
  if (!P)
    printf("0 0\n");
  else {
    int flag=0;
    for (; P; P=P->link){
      if (!flag)
        flag = 1;
      else 
        printf(" ");
      printf("%d %d", P->coef, P->expon);
    }
    printf("\n");
  }
}
