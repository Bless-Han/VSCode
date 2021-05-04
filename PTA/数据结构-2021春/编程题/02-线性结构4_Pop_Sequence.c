#include <stdio.h>
#include <stdbool.h>

int main(){
  int M,N,K;
  scanf("%d %d %d", &M, &N, &K);
  int stack[M], pool[N];
  bool flag;
  while (K--){
    flag = true;
    for (int i=0; i<N; i++){
      scanf("%d", &pool[i]);
    }
    int pPool=0;
    int pStack=-1;
    int num=1;
    while(pPool < N){
      if (pStack == -1)
        stack[++pStack] = num++;
      else {
        if (stack[pStack] == pool[pPool]) {
          pStack--;
          pPool++;
        } else if(stack[pStack] < pool[pPool]){
          if ((++pStack) == M){
            flag = false;
            break;
          }
          stack[pStack] = num++;
        } else {
          flag = false;
          break;
        }
      }
    }
    if (flag) puts("YES");
    else puts("NO");
  }
  return 0;
}
