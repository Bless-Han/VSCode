#include <iostream>
using namespace std;
int main(){
  string month[3]
  {
    "Jan",
      "Feb",
      "Mar"
  };
  int sum = 0;
  int temp;
  for (string s : month){
    cout << s << ": ";
    cin >> temp;
    sum += temp;
  }
  cout << "sum = " << sum << endl;
  return 0;
}
