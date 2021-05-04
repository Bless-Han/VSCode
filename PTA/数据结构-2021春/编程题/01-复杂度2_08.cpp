#include <iostream>
using namespace std;

int main(void)
{
  int k;
  cin >> k;
  int a[k];
  int thisSum, maxSum, left, right;
  thisSum = maxSum = left = right = 0;
  int flagNegative = 1;
  int count = 0;
  for (int i=0; i<k; i++){
    cin >> a[i];
    if (a[i] >= 0) flagNegative = 0;
    thisSum += a[i];
    count++;
    if (thisSum < 0)
      count = thisSum = 0;
    if (thisSum > maxSum){
      maxSum = thisSum;
      right = a[i];
      left = a[i - count + 1];
    }
  }
  if (flagNegative && k){
    left = a[0];
    right = a[k-1];
  }
  printf("%d %d %d\n", maxSum, left, right);
  return 0;
}
