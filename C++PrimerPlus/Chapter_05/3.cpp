#include <iostream>
using namespace std;
int main(){
  int count = 1;
  int temp;
  cin >> temp;
  while(temp != 0)
  {
    cout << count++ << endl;
    cin >> temp;
  }
  return 0;
}
