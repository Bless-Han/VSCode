#include <iostream>
using namespace std;

int main(){
  cout << "Enter your age: ";
  int age;
  cin >> age;
  int months = age * 12;
  cout << age << " age contain "
    << months << " months.\n";
  return 0;
}
