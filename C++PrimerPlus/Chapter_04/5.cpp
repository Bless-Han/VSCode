#include <iostream>
using namespace std;
struct CandyBar{
  string name;
  double weight;
  int kalu;
};
int main(){
  CandyBar snack{"Mocha Munch", 2.3, 350};
  cout << "name = " << snack.name 
    << "\nweight = " << snack.weight 
    << "\nkalu = " << snack.kalu << endl;
  return 0;
}
