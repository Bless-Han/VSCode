#include <iostream>
using namespace std;

int check();
int m, n, k;
int main(){
  cin >> m >> n >> k;
  for (int i=0; i<k; i++){
    if (check() == 1) puts("YES");
    else puts("NO");
  }
  return 0;
}
int check(){
  int i;
  int y[n]; // 表示读取的数据
  int s[m]; // 表示堆栈
  int sIndex = 0; // 堆栈下标
  int sData = 1; // 表示要压入堆栈的有序序列，如 1 - 7
  for (i=0; i<n; i++)
    scanf("%d", &y[i]);
  for (i=0; i<n; i++) { // i同时表示读取数据(y[i])的下标
    while (sData <= y[i]){ // 如果有序序列当前的数小于等于tmp,则 push
      if (sIndex >= m) goto END; //  如果下标越界
      else s[sIndex++] = sData++;
    }
    if (s[sIndex - 1] == y[i] && sIndex > 0) sIndex--; // 如果堆栈top == tmp 则 pop 
    if (s[sIndex - 1] > y[i] && sIndex > 0) break; // 如果堆栈top > tmp 则条件不成立
  }
END:
  if (sIndex == 0 && sData == n + 1) return 1;  // 如果堆栈为状态为空，且有序序列中所有数据都压出去
  else return 0;
}
