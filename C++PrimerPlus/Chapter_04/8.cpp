#include <iostream>
using namespace std;
const int N = 20;
struct Pizza{
  char name[N];
  double length;
  double weight;
};
int main(){
  Pizza * p = new Pizza;
  cin >> p->length;
  cin.get();
  cin.getline((p)->name, N);
  cin >> p->weight;
  cout << "--------------------\n";
  cout << p->name << endl 
    << p->length << endl 
    << p->weight << endl;
  delete p;
  return 0;
}
