#include <iostream>
using namespace std;
int change(int celsius);
int main(){
  cout << "Please enter a Celsius value: ";
  int celsius;
  cin >> celsius;
  cout << celsius << " degrees Cellsius is "
    << change(celsius) << " degrees Fahrenheit.\n";
  return 0;
}
int change(int celsius){
  return celsius * 1.8 + 32;
}
