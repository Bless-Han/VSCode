#include <stdio.h>
#define MAXN 100001

int main(){
  int k, tmp;
  int nowSum, maxSum;
  nowSum=maxSum=0;
  scanf("%d", &k);
  for (int i=0; i<k; i++){
    scanf("%d", &tmp);
    nowSum+=tmp;
    if (nowSum<0) nowSum=0;
    if (nowSum>maxSum) maxSum=nowSum;
  }
  printf("%d\n", maxSum);
  return 0;
}
