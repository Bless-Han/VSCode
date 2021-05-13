#include <iostream>
using namespace std;
template <class T>
T maxa(T x, T y)
{
  return x > y ? x : y;
}
int main()
{
  int a = 20;
  int b = 90;
  cout << maxa (a, b) << endl;
  return 0;
}