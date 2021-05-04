#include <iostream>
using namespace std;

int main(){
  int a, b;
  int sum = 0;
  cin >> a >> b;
  for ( ; a <= b; ++a)
    sum += a;
  cout << sum;
  return 0;
}
