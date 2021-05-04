#include <iostream>
using namespace std;
const int Year = 3;
int main(){
  string month[3]
  {
    "Jan",
      "Feb",
      "Mar"
  };
  int sum[Year]{};
  int temp;
  for (int i = 0; i < Year; ++i)
  {
    for (string s : month)
    {
      cout << i + 1 << " year, "<< s << ": ";
      cin >> temp;
      sum[i] += temp;
    }
  }
  int sumSum{};
  for (int i = 0; i < Year; ++i)
  {
    cout << "sum " << i << " = " << sum[i] << endl;
    sumSum += sum[i];
  }
  cout << "sumSum = " << sumSum << endl;
  return 0;
}
