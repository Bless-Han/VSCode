#include <iostream>
using namespace std;
int f(int x);
int main()
{
  cout << "Hello World!!\n";
  int x;
  cin >> x;
  cout << x << endl;
  return 0;
}
int f(int x)
{
  return x >= 0 ? x : -x;
}
