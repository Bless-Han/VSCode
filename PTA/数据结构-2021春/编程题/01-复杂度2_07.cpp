#include <iostream>
#define MAXN 10001

int main(void) {
  int k;
  int a[MAXN];
  int count = 0;
  int maxSum, thisSum, left, right;
  int flagNegative = 1;
  scanf("%d", &k);
  maxSum = thisSum = left = right = 0;
  for (int i=0; i<k; i++){
    scanf("%d", &a[i]);
    thisSum += a[i];
    count++;
    if (a[i] >= 0) flagNegative = 0;
    if (thisSum < 0) count = thisSum = 0;
    if (thisSum > maxSum) {
      maxSum = thisSum;
      right = a[i];
      left = a[i - count + 1];
    }
  }
  if (flagNegative && k){
    left = a[0];
    right = a[k - 1];
  }
  printf("%d %d %d\n", maxSum, left, right);
  return 0;
}
