#include <stdio.h>

int f(int n, char c);
void printSps(int i);
void printC(int i, char c);
int main(){
  int n, m;
  m = n = 0;
  char c;
  scanf("%d %c", &n, &c);
  m = f(n, c);
  printf("%d", m);
  return 0;
}
int f(int n, char c){
  int sum = 1;
  int next = 6;
  int i = 1;
  int ret = 0;
  if (n > 0) {
    while (sum + next <= n){
      i++;
      sum += next;
      next += 4;
    }
    ret = n - sum;

    for(int j = 0; j < i; j++){
      printSps(j);
      printC(i - j, c);
    }
    for (int j = 1; j < i; j++){
      printSps(i - j - 1);
      printC(j + 1, c);
    }
  }
  return ret;
}
void printC(int i, char c){
  for (int j = 0; j < i * 2 - 1; j++)
    printf("%c", c);
  printf("\n");
}
void printSps(int i){
  for (int j = 0; j < i; j++){
    printf(" ");
  }
}
