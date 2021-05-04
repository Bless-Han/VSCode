#include <iostream>
using namespace std;
struct CandyBar{
  string name;
  double weight;
  int kalu;
};
int main(){
  CandyBar * a = new CandyBar[3];
  for (int i=0; i<3; i++)
    cout << "name = " << a[i].name 
      << "\nweight = " << a[i].weight 
      << "\nkalu = " << a[i].kalu << endl;

  return 0;
}
