#include <iostream>
using namespace std;
double change(double x);
int main(){
  cout << "Enter the number of light years: ";
  double n;
  cin >> n;
  cout << n << " light years = "
    << change(n) << " astronomical units.\n";
  return 0;
}
double change(double x){
  return x * 63240;
}
