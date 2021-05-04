#include <iostream>
using namespace std;

int m, n, k;
int check();
int main(){
  cin>>m>>n>>k;
  for (int i=0; i<k; i++){
    if (check()) puts("YES");
    else puts("NO");
  }
  return 0;
}
int check(){
  int s[n];
  int sIndex = 0;
  int x=1;
  int y[n];
  for (int i=0; i<n; i++)
    cin>>y[i];
  for (int i=0; i<n; i++){
    while(x<=y[i]){
      if (sIndex >= m) goto END;
      else s[sIndex++] = x++;
    }
    if (s[sIndex-1] == y[i]) sIndex--;
    else if(s[sIndex-1] > y[i]) break;
  }
END:
  if (sIndex == 0 && x-1 == n) return 1;
  return 0;
}
