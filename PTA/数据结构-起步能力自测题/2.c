#include <stdio.h>
#define MAXN 100001

int a[MAXN];
int f(int n);

int main(void){
  for (int i = 0; i < MAXN; i++){
    a[i] = 1;
  }
  a[0] = a[1] = 0;
  for (int i = 2; i * 2 <= MAXN; i++){
    for (int j = i * 2; j <= MAXN; j += i){
      if (a[j] != 0)
        a[j] = 0;
    }
  }

  int n;
  scanf("%d", &n);
  int x = f(n);
  printf("%d", x);
  return 0;
}
int f(int n){
  int ret = 0;
  if (n % 2 == 0)
    n--;
  for ( ; n >= 5; n--){
    if (a[n] == 1 && a[n - 2] == 1)
      ret++;
  }
  return ret;
}
