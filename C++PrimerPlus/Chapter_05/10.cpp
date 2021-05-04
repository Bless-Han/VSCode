#include <iostream>
using namespace std;
int main()
{
  cout << "Enter number of rows:";
  int rows{};
  cin >> rows;
  for (int i = 1; i <= rows; ++i)
  {
    for (int j = rows - i; j; --j)
      cout << ".";
    for (int aste = i; aste; --aste)
      cout << "*";
    cout << endl;
  }
  return 0;
}
