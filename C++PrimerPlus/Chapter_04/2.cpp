#include <iostream>
using namespace std;
int main(){
  // const int ArSize = 20;
  // char name[ArSize];
  // char dessert[ArSize];
  string name;
  string dessert;

  cout << "Enter your name:\n";
  getline(cin, name);
  cout << "Enter your favorite dessert:\n";
  getline(cin, dessert);
  cout << "I ahve some delicious " << dessert;
  cout << " for you, " << name << ".\n";
  return 0;
}
