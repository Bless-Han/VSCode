#include <iostream>
int main(){
  using namespace std;
  int feet, inches, pounds;
  cin >> feet >> inches >> pounds;
  double meter = (feet * 12 + inches) * 0.0254;
  double kg = pounds / 2.2;
  cout << kg / (meter * meter);
  return 0;
}
