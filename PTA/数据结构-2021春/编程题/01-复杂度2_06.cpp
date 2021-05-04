#include <iostream>
#define MAXN 10001
using namespace std;

int main(void) {
  int k;
  int a[MAXN];
  int thisSum, maxSum, left, right;
  int flagNegative = 1;
  int count =0;
  thisSum=maxSum=left=right=0;
  cin >> k;
  for (int i=0; i<k; i++){
    cin >> a[i];
    thisSum+=a[i];
    if (a[i] >= 0) flagNegative = 0;
    count++;
    if (thisSum < 0){
      thisSum = count = 0;
    }
    if (thisSum > maxSum){
      maxSum = thisSum;
      right = a[i];
      left = a[i-count+1];
    }
  }
  if (flagNegative && k){
    left = a[0];
    right = a[k-1];
  }
  printf("%d %d %d\n", maxSum, left, right);
  return 0;
}
