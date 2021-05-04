#include <iostream>
using namespace std;
const int N = 10;
int main()
{
  double donation[N]{};
  double temp{};
  double sum{};
  int i;
  for (i = 0; i < N; i++)
  {
    if (cin >> temp)
    {
      donation[i] = temp;
      sum += temp;
    }
    else 
      break;
  }
  double average = sum / i;
  cout << "Average = " << average << endl;
  int count{};
  for (int j = 0; j < i; ++j)
    if (donation[j] > average)
      count++;
  cout << "Count = " << count << endl;
  return 0;
}
