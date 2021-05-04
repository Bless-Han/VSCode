#include <iostream>
using namespace std;
int change(int n);
int main(){
  cout << "Please enter a long: ";
  int l;
  cin >> l;
  int mar = change(l);
  cout << l << " long = "
    << mar << "mar.\n";
  return 0;
}
int change(int n){
  return n * 220;
}
