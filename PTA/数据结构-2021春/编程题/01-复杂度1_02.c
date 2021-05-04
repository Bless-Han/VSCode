#include <stdio.h>

int main(){
  int n;
  scanf("%d", &n);
  int nowSum, maxSum, tmp;
  nowSum = maxSum = 0;
  for (int i=0; i<n; i++){
    scanf("%d", &tmp);
    nowSum += tmp;
    if (nowSum < 0) nowSum = 0;
    if (nowSum > maxSum) maxSum = nowSum;
  }
  printf("%d\n", maxSum);
  return 0;
}
