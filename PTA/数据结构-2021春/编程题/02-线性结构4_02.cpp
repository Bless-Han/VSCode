#include <iostream>
using namespace std;

int m, n, k;
int check();
int main(void)
{
  cin >> m >> n >> k;
  for (int i=0; i<k; i++){
    if (check()) puts("YES");
    else puts("NO");
  }
  return 0;
}
int check(){
  int i;
  int y[n];
  int s[m];
  int sIndex = 0;
  int x = 1;
  for (i=0; i<n; i++)
    scanf("%d", &y[i]);
  for (i=0; i<n; i++){
    while(x <= y[i]){
      if (sIndex >= m) goto END;
      s[sIndex++] = x++;
    }
    if (s[sIndex - 1] == y[i]) sIndex--;
    if (s[sIndex - 1] > y[i] && sIndex > 0) break;
  }
END:
  if (sIndex == 0 && x == n + 1) return 1;
  else return 0;
}
