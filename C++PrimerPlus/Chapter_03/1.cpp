#include <iostream>
int main(){
  using namespace std;
  const int Inch_per_foot = 12;
  int height{0};
  cout << "Enter your height:______\b\b\b\b\b\b";
  cin >> height;
  int foot = height / Inch_per_foot;
  int inch = height % Inch_per_foot;
  cout << "Your height " << foot << " foot,"
    << inch << " inch.\n";
  return 0;
}
