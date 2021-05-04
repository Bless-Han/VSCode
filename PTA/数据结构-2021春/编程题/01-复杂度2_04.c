#include <stdio.h>
#define MAXN 10001

int main(void){
  int k;
  int a[MAXN];
  int left,right, thisSum, maxSum;
  left=right=thisSum=maxSum=0;
  int count = 0;
  int flagNegative = 1;
  scanf("%d", &k);
  for (int i=0; i<k; i++){
    scanf("%d", &a[i]);
    if (a[i] >= 0)
      flagNegative = 0;
    thisSum += a[i];
    count++;
    if (thisSum < 0)
      count=thisSum=0;
    if (thisSum > maxSum){
      left=a[i-count+1];
      maxSum = thisSum;
      right=a[i];
    }
  }
  if (flagNegative){
    left = a[0];
    right = a[k - 1];
  }
  printf("%d %d %d\n", maxSum, left, right);
  return 0;
}
